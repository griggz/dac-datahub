from django.db import models


class Subscribe(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Subscribe")
        verbose_name_plural = ("Subscriptions")
        ordering = ["-date_created"]

    def __str__(self):
        return self.email
