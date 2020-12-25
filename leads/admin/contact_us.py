from django.contrib import admin
from django.db import models
from leads.models import ContactUs
from pagedown.widgets import AdminPagedownWidget


class ContactUsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ["organization", "first_name", "last_name"]
    list_filter = ["organization"]
    search_fields = ["organization"]
    ordering = ['contact_date']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)