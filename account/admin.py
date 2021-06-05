from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

# Register your models here.

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Change', {
            'fields': ['avatar']
        }),
    )

admin.site.register(CustomUserModel, CustomAdmin) 