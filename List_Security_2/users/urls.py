from django.urls import path

from . import views

yubikey_urls = [
    path('yubikey/register', views.YubiKeyRegisterView.as_view(), name='yubikey-register'),
    path('yubikey/verify', views.YubiKeyLoginView.as_view(), name='yubikey-verify'),
    path('yubikey/remove', views.YubiKeyRemovalView.as_view(), name='yubikey-remove'),
]

urlpatterns = [
                  path('signup/', views.SignUp.as_view(), name='signup'),
              ] + yubikey_urls
