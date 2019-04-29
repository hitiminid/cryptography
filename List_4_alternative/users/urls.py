from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('yubikey/register', views.YubiKeyRegister.as_view(), name='yubikey-register'),
    path('yubikey/verify', views.YubiKeyLogin.as_view(), name='yubikey-verify'),
]
