from django.urls import re_path, path
from leads.api.views import ContactUsListCreate, ContactUsRecord, SubscribeListCreate, SubscribeRecord

app_name = 'leads-api'

urlpatterns = [
    # CONTACT US
    path('contact_us/', ContactUsListCreate.as_view(), name='contact_us-list'),
    re_path(r'^contact_us/(?P<id>[\w-]+)/$', ContactUsRecord.as_view(), name='contact_us-record'),
    # SUBSCRIBE
    path('subscribe/', SubscribeListCreate.as_view(), name='subscribe-list'),
    re_path(r'^subscribe/(?P<id>[\w-]+)/$', SubscribeRecord.as_view(), name='subscribe-record'),
]
