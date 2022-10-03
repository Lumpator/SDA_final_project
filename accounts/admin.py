from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserPermissions


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', "permission"
        # 'is_teacher', 'is_student', 'mailing_address'
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Custom Permission status', {
            'fields': ('permission',)
        }),
        # ('Permissions', {
        #     'fields': (
        #         'is_active', 'is_staff', 'is_superuser',
        #         'groups', 'user_permissions'
        #         )
        # }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Custom Permission status', {
            'fields': ('permission')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        # ('Permissions', {
        #     'fields': (
        #         'is_active', 'is_staff', 'is_superuser',
        #         'groups', 'user_permissions'
        #         )
        # }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),

    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserPermissions)
