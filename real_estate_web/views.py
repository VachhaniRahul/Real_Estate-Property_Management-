from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from datetime import datetime
from real_estate_web.models import Contact_us, Property_Inquiry
from django.contrib import messages
# from .models import Profile
import uuid
from .utils1 import *
from django.core.mail import send_mail
from django.conf import settings
from .utils1 import send_email_token
from .forms import RegisterForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import OtpToken, Property_details
import secrets
import random

# User testing password = Abcd123@

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")

    property_details = list(Property_details.objects.all())

    property_details_homepage = random.sample(property_details, 5)
    print("Property_details: ", property_details_homepage)

    # print("Property_details", property_details_homepage, property_details_homepage.price, property_details_homepage.desc)

    param = {
        'property_details': property_details_homepage,
    }

    print("The value is ", param['property_details'])
    print("The sample is ", property_details_homepage)

    return render(request, "index.html", param)

def about(request):
    return render(request, "about.html")

def contact_us(request):
    if request.method == "POST":
        phone =  request.POST.get('phone')
        interact_as = request.POST.get('interact_as')
        email_address = request.POST.get('email_address')
        message =  request.POST.get('message')
        
        contact_us = Contact_us(phone = phone, interact_as = interact_as, email_address = email_address, message = message, date = datetime.today())
        contact_us.save()
        messages.success(request, "Your Message has been sent.")
    return render(request, "contact_us.html")
        

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! An OTP was sent to your Email")
            return redirect("verify-email", username=request.POST['username'])
    context = {"form": form}
    return render(request, "signup.html", context)




def verify_email(request, username):
    user = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
    
    
    if request.method == 'POST':
        # valid token
        if user_otp.otp_code == request.POST['otp_code']:
            
            # checking for expired token
            if user_otp.otp_expires_at > timezone.now():
                user.is_active=True
                user.save()
                messages.success(request, "Account activated successfully!! You can Login.")
                return redirect("signin")
            
            # expired token
            else:
                messages.warning(request, "The OTP has expired, get a new OTP!")
                return redirect("verify-email", username=user.username)
        
        
        # invalid otp code
        else:
            messages.warning(request, "Invalid OTP entered, enter a valid OTP!")
            return redirect("verify-email", username=user.username)
        
    context = {}
    return render(request, "verify_token.html", context)




def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST["otp_email"]
        
        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            
            # email variables
            subject="Email Verification"
            message = f"""
                                Hi {user.username}, here is your OTP {otp.otp_code} 
                                it expires in 5 minute, use the url below to redirect back to the website
                                http://127.0.0.1:8000/verify-email/{user.username}
                                
                                """
            sender = "eshopweb2901@gmail.com"
            receiver = [user.email, ]
        
        
            # send email
            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False,
                )
            
            messages.success(request, "A new OTP has been sent to your email-address")
            return redirect("verify-email", username=user.username)

        else:
            messages.warning(request, "This email dosen't exist in the database")
            return redirect("resend-otp")
        
           
    context = {}
    return render(request, "resend_otp.html", context)




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            messages.success(request, f"Hi {request.user.username}, you are now logged-in")
            return redirect("/")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("signin")
        
    return render(request, "login.html")

def search(request):
    query=request.GET['query']
    print("Query is: ", query)
    if len(query)>78:
        allPosts=Property_details.objects.none()
    else:
        allPostsTitle= Property_details.objects.filter(property_name__icontains=query)
        allPostsCategory= Property_details.objects.filter(category__icontains=query)
        # allPostsSubcategory= Property_details.objects.filter(subcategory__icontains=query)
        allPostsContent = Property_details.objects.filter(desc__icontains=query)
        allPostsPrice = Property_details.objects.filter(price__icontains=query)
        allPostsAddress = Property_details.objects.filter(address__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent).union(allPostsCategory).union(allPostsPrice).union(allPostsAddress)#.union(allPostsSubcategory)
        
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)


def profile(request):
    return render(request, "profile.html")

def view_property(request, view_property_page_property_id):
    print("Property id is: ", view_property_page_property_id)
    view_property = Property_details.objects.filter(id = view_property_page_property_id)
    print("view_property: ", view_property)
    print("view_property[0]: ",view_property[0])
    total_images = [1, 2, 3, 4, 5]
    loop_through = [1, 2, 3, 4, 5]
    return render(request, "view_property.html", {'view_property': view_property[0], 'total_images': total_images, 'loop_through': loop_through})

def inquiry(request, inquiry_page_property_id):
    
    print("This is Inquiry:")
    if request.method == 'POST':
        inquiry_name = request.POST.get('inquiry_name')
        inquiry_email_address = request.POST.get('email_address')
        inquiry_phone_number = request.POST.get('phone')
        inquiry_property_name = request.POST.get('property_name')
        property_id = request.POST.get('property_id')

        print('Detail is: ', inquiry_name, inquiry_email_address, inquiry_phone_number, inquiry_property_name, property_id)
        
        property_inquiry = Property_Inquiry(inquiry_name = inquiry_name, inquiry_email_address = inquiry_email_address, inquiry_phone_number = inquiry_phone_number, inquiry_property_name = inquiry_property_name, property_id = property_id)

        property_inquiry.save()
        messages.success(request, "Your Message has been sent.")

        return redirect("/")
    
    print("Property id is: ", inquiry_page_property_id)
    inquiry_property = Property_details.objects.filter(id = inquiry_page_property_id)
    print("Property id is: ", inquiry_property[0])

    return render(request, "inquiry.html", {'inquiry_property': inquiry_property[0]})














































# def loginUser(request):
#     if request.method == "POST":
#         # check if user has entered correct credentials
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # print(username, password)
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             return render(request, "login.html")
#     return render(request, "login.html")

# def logoutUser(request):
#     logout(request)
#     return redirect("/login")

# def signup(request):

    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user_obj = User(username = email)
    #     user_obj.set_password(password)

    #     print(user_obj)
    #     print(str(uuid.uuid4))

    #     p_obj = Profile.objects.create(user = user_obj, email_token = str(uuid.uuid4()))
    #     send_email_token(email, p_obj.email_token)
    # return 0

    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Account created successfully! An OTP was sent to your Email")
    #         return redirect("verify-email", username = request.POST['username'])
    # context = {"form": form}
    # return render(request, "signup.html", context)

# def verify_email(request, username):
#     user = get_user_model().objects.get(username=username)
#     user_otp = OtpToken.objects.filter(user=user).last()
#     if request.method == 'POST':
#         if user_otp.otp_code == request.POST['otp_code']:

#             # valid token
#             if user_otp.otp_expires_at > timezone.now():
#                 user.is_active=True
#                 user.save()
#                 messages.success(request, "Account activated successfully!! You can Login.")
#                 return redirect("signin")
            
#             # expired token
#             else:
#                 messages.warning(request, "The OTP has expired, get a new OTP!")
#                 return redirect("verify-email", username=user.username)
        
#         # invalid otp code
#         else:
#             messages.warning(request, "Invalid OTP entered, enter a valid OTP!")
#             return redirect("verify-email", username=user.username)
        
#     context = {}
#     return render(request, "verify_token.html", context)


# def verify(request, token):
#     try:
#         obj = Profile.objects.get(email = token)
#         obj.is_verified = True
#         obj.save()
#         return HttpResponse('Your accound verified')

#     except:
#         return HttpResponse("Invalid token")
    
# def profile(request):
#     return render(request, "profile.html")