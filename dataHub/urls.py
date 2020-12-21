from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

from .views import portal_redirect

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,),
   authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    re_path(r'^api/docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ACCOUNTS & AUTHENTICATION
    re_path(r'^account/', include("accounts.urls", namespace='account')),
    re_path(r'^accounts/', include("accounts.passwords.urls")),
    re_path(r'^accounts/$', RedirectView.as_view(url='/account')),
    path('', portal_redirect, name='portal_redirect')
]
