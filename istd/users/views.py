import json
from hashlib import md5

from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.http import HttpResponseBadRequest
# from s.views import BT
# from s.views import get_city
from . import models
from .forms import RegisterForm, LoginForm
from main.views import BaseView
# from .forms import LoginForm, RegisterForm, ChangeUserInfo, ChangeUserProfile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            raise HttpResponseBadRequest()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # url_activated = request.get_host() + str(reverse('users:after_register', kwargs={'activation_url': md5(str(request.COOKIES['sessionid']).encode('utf-8')).hexdigest()}))
            similar_users = models.User.objects.get(email=email)
            if similar_users:
                raise ValueError('Пользователь с таким email уже существует')
            user = models.User.objects.create_user(email=email, password=password)
            user.save()

            user = auth.authenticate(email=email, password=password)
            if user is None:
                messages.add_message(request, messages.ERROR, 'Неверный логин или пароль')
                raise ValueError('Неверный логин или пароль')
            else:
                auth.login(request=request, user=user)
                message = {'msg': 'Вы успешно зарегистрированы, не забудьте проверить свою электронную почту!'}
                html = render_to_string('base.html', {'msg': messages})
                print(HttpResponse(json.dumps(html).encode('utf-8')))
                return HttpResponse(HttpResponse(json.dumps(html).encode('utf-8')))


def after_register(request, activation_url):
    url_activated = request.get_host() + str(reverse('users:after_register', kwargs={'activation_url': activation_url}))
    profiles_count = models.User.objects.filter(activation_link__exact=url_activated).count()
    if profiles_count == 0:
        raise Http404

    profile = models.User.objects.filter(activation_link__exact=url_activated)[:1]
    for pro in profile:
        pro.is_confirm = True
        pro.activation_link = None
        pro.save()
    message = {'msg', 'Ваша учётная запись успешно активирована'}

    return render(request.get_host() + reverse('users:activated'), template_name='index.html', context=message)


def forgot_password(request):
    pass


def change_password(request):
    pass


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                if request.is_ajax():
                    j_ = json.dumps({'status': 200, 'message': 'Вы успешно авторизированы',
                                     'html': render_to_string('_components/header_nav.html', {'request': request, 'user_city': get_city(request)})}, ensure_ascii=False)
                    j_.encode('utf-8')
                    return JsonResponse(j_, safe=False)
                else:
                    return HttpResponseRedirect(reverse('index'))
            else:
                j_ = json.dumps({'status': 400, 'message': 'Неверный логин или пароль'}, ensure_ascii=False)
                j_.encode('utf-8')
                return JsonResponse(j_, safe=False)
        else:
            print(form.errors)
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class UserCabinetTemplate(BaseView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwards):
        context = super(UserCabinetTemplate, self).get_context_data(**kwards)
        context['user'] = self.request.user

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return super(UserCabinetTemplate, self).dispatch(request, *args, **kwargs)


class UserCabinetChangeTemplate(UserCabinetTemplate):
    template_name = 'users/account.html'

    def get_context_data(self, **kwards):
        context = super(UserCabinetChangeTemplate, self).get_context_data(**kwards)
        context['user_data'] = self.request.user.objects

        return context

