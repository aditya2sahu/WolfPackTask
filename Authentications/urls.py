
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # Sing Up
    path('sing_up',views.sing_up,name='sing_up'),
    # login
    path('login',views.login,name='login'),
    # Refresh Token 
    path('refresh_token',TokenRefreshView.as_view(),name='refresh_token'),
]