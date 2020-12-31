from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.sessions.models import Session

from django.contrib import admin
from django.db import models

from .forms import UserChangeForm, UserRegisterForm, GroupAdminForm
from .models import User, Apps


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserRegisterForm

    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active', 'nickname')
    # list_select_related = (Token,)
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'nickname', 'password', 'meta', 'slug', 'last_login'),}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    readonly_fields = ['slug']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'email2', 'password1', 'password2', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)

