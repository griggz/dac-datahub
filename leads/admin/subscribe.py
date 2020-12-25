from django.contrib import admin
from django.db import models
from leads.models import Subscribe
from pagedown.widgets import AdminPagedownWidget


class SubscribeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ["email", "date_created"]
    list_filter = ["email"]
    search_fields = ["email"]
    ordering = ['date_created']

    class Meta:
        model = Subscribe


admin.site.register(Subscribe, SubscribeAdmin)