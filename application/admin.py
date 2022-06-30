from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'points', 'profile')
    list_filter = ('email', 'is_staff', 'is_active', 'points', 'profile')
    fieldsets = (
        (None, {'fields': ('email', 'nickname', 'password', 'first_name', 'last_name', 'points', 'profile')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active',  'points', 'profile')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'nickname')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
