from django.db import models


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=300, blank=True, null=True)
    organization = models.CharField(max_length=300, blank=True, null=True)
    work_phone = models.CharField(max_length=100, blank=True, null=True)
    web_site = models.CharField(max_length=1000, blank=True, null=True)
    number_of_staff = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=300, blank=True, null=True)
    solution_option = models.CharField(max_length=300, blank=True, null=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    method_of_referral = models.CharField(max_length=300, blank=True, null=True)
    contact_source = models.CharField(max_length=100, blank=True, null=True)
    additional_details = models.TextField(default='')

    class Meta:
        verbose_name = ("Contact Us")
        verbose_name_plural = ("Contact Us")
        ordering = ["-contact_date"]

    def __str__(self):
        return self.organization
