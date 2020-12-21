from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import (login_view, register_view, logout_view)
from accounts.api.views import (AuthAPIView, fetch_account, AuthDetailAPIView, registration)

app_name = 'accounts'

urlpatterns = [
    # Local Views
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^register/$', register_view, name='register'),
    # API Views
    path('api/', AuthAPIView.as_view(), name='auth-list'),
    re_path(r'^api/account/(?P<slug>[\w-]+)/$', AuthDetailAPIView.as_view(), name='auth-detail'),
    path('api/account/', fetch_account, name='auth-fetch'),
    path('api/register/', registration, name='registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
