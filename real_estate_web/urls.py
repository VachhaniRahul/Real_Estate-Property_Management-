from django.contrib import admin
from django.urls import path, include
from real_estate_web import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("about", views.about, name = "about"),
    path("contact_us", views.contact_us, name = "contactus"),
    path("signup", views.signup, name = "signup"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("signin", views.signin, name = "signin"),
    # path("verify", views.verify, name="verify"),
    # path("logout", views.logoutUser, name="logout"),
    path("profile", views.profile, name="profile"),
    path("view_property/<int:view_property_page_property_id>", views.view_property, name="view_property"),
    path("search", views.search, name = "search"),
    path("inquiry/<int:inquiry_page_property_id>", views.inquiry, name="inquiry"),
]