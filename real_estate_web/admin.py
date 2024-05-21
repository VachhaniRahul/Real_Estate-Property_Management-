from django.contrib import admin
from real_estate_web.models import Contact_us, CustomUser, OtpToken, Property_details, Property_Inquiry
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )


class OtpTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_code")

admin.site.register(Contact_us)
admin.site.register(Property_details)

admin.site.register(OtpToken, OtpTokenAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Property_Inquiry)