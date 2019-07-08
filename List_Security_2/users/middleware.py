from django.shortcuts import redirect
from django.urls import resolve
from users.models import YubiKeyDevice


def yubikey_verification(get_response):

    def middleware(request):

        if not request.user.is_authenticated:
            return get_response(request)

        user_has_yubikey = YubiKeyDevice.objects.filter(user=request.user).exists()

        if not user_has_yubikey:
            return get_response(request)

        is_yubikey_verification = resolve(request.path_info).url_name == 'yubikey-verify'

        if is_yubikey_verification:
            return get_response(request)

        is_yubikey_verified = request.session.get('yubikey_verified')

        if is_yubikey_verified:
            return get_response(request)

        return redirect('yubikey-verify')

    return middleware
