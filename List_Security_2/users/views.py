import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from u2flib_server import u2f

from .forms.RegistrationForm import RegistrationForm
from .models import YubiKeyDevice


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


def get_origin(request):
    return f'{request.scheme}://{request.get_host()}'


class YubiKeyRegisterView(View):

    def get(self, request, *args, **kwargs):
        app_id = get_origin(request)
        challenge = u2f.begin_registration(app_id)
        request.session['challenge'] = challenge
        json_challenge = json.dumps(challenge)
        context = {'challenge': json_challenge}

        return render(request, 'add_yubikey.html', context)

    def post(self, request, *args, **kwargs):
        u2f_response = request.POST['response']
        u2f_request = request.session['challenge']
        device, _ = u2f.complete_registration(u2f_request, u2f_response)

        yubikey_data = {
            'app_id': device['appId'],
            'public_key': device['publicKey'],
            'key_handle': device['keyHandle'],
        }

        YubiKeyDevice.objects.update_or_create(user=request.user, defaults=yubikey_data)

        messages.add_message(request, messages.INFO, 'Your YubiKey has been registered!')
        del request.session['challenge']

        request.session['yubikey_verified'] = True
        request.session['has_yubikey'] = True

        return redirect('home')


class YubiKeyLoginView(View):

    def get(self, request, *args, **kwargs):
        device = YubiKeyDevice.objects.filter(user=request.user).first()

        if not device:
            request.session['has_yubikey'] = False
            return redirect('home')

        challenge_data = [{
            'appId': device.app_id,
            'keyHandle': device.key_handle,
            'publicKey': device.public_key,
            'version': 'U2F_V2'
        }]

        challenge = u2f.begin_authentication(device.app_id, challenge_data)
        request.session['challenge'] = challenge
        context = {'challenge': json.dumps(challenge)}

        return render(request, 'check_yubikey.html', context)

    def post(self, request, *args, **kwargs):
        u2f_response = request.POST['response']
        u2f_request = request.session['challenge']
        device, counter, _ = u2f.complete_authentication(u2f_request, u2f_response)
        messages.add_message(request, messages.INFO, 'Your YubiKey has been verified!')
        del request.session['challenge']
        request.session['yubikey_verified'] = True
        request.session['has_yubikey'] = True

        return redirect('home')


class YubiKeyRemovalView(View):

    def get(self, request, *args, **kwargs):

        device = YubiKeyDevice.objects.filter(user=request.user).first()

        if not device:
            request.session['yubikey_verified'] = False
            return redirect('home')

        challenge_data = [{
            'appId': device.app_id,
            'keyHandle': device.key_handle,
            'publicKey': device.public_key,
            'version': 'U2F_V2'
        }]

        challenge = u2f.begin_authentication(device.app_id, challenge_data)

        request.session['challenge'] = challenge
        context = {'challenge': json.dumps(challenge)}
        return render(request, 'check_yubikey.html', context)

    def post(self, request, *args, **kwargs):

        u2f_response = request.POST['response']
        u2f_request = request.session['challenge']
        device, counter, _ = u2f.complete_authentication(u2f_request, u2f_response)
        messages.add_message(request, messages.INFO, 'YubiKey has been removed!')
        del request.session['challenge']
        request.session['yubikey_verified'] = True

        yubikey_device = YubiKeyDevice.objects.filter(user=request.user).first()

        if yubikey_device:
            yubikey_device.delete()

        request.session['has_yubikey'] = False

        return redirect('home')
