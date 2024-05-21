from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import secrets
import random

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     email_token = models.CharField(max_length = 500, null = True, blank=True)
#     is_verified = models.BooleanField(default = False)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = ("email")
    REQUIRED_FIELDS = ["username"]
    
    def _str__(self):
        return self.email
    

class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    tp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username


class Property_details(models.Model):
    property_id = models.AutoField
    property_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=400)
    publish_date = models.DateField(null=True)
    address = models.CharField(max_length=50)

    image = models.ImageField(upload_to = 'uploaded_image', max_length=100, null=False, blank=False)

    image1 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image2 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image3 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image4 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image5 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image6 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image7 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image8 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image9 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image10 = models.ImageField(upload_to = 'uploaded_image', default = "")
    image11 = models.ImageField(upload_to = 'uploaded_image', default = "")

    def __str__(self):
        return self.property_name

class Contact_us(models.Model):
    email_address = models.EmailField(default = "")
    interact_as = models.CharField(max_length=10, default = "")
    phone = models.CharField(max_length = 15)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.phone
    
class Property_Inquiry(models.Model):
    inquiry_name = models.CharField(max_length = 20)
    inquiry_email_address = models.CharField(max_length = 50)
    inquiry_phone_number = models.CharField(max_length = 15)
    inquiry_property_name = models.CharField(max_length = 30)
    property_id = models.CharField(max_length = 5)

    def __str__(self):
        return self.inquiry_name