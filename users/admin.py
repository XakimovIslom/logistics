from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


class AccountAdmin(BaseUserAdmin):
    list_display = ('id', 'username')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'full_name', 'phone', 'image', 'password')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                       'groups', 'user_permissions')}),
        # (_('Important dates'), {'fields': ('created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2'), }),
    )
    search_fields = ('username', 'email', 'full_name', 'phone')


admin.site.register(User, AccountAdmin)
