from django.contrib import auth
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.views import BaseView
from . import models


# from .forms import LoginForm, RegisterForm, ChangeUserInfo, ChangeUserProfile


# Create your views here.
def get_object_or_none(klass, *args, **kwargs):
    try:
        return klass._default_manager.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None


def register(request):
    if request.method == 'POST':
        fio = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        about = request.POST['about']
        avatar = request.FILES['avatar'].name
        # url_activated = request.get_host() + str(reverse('users:after_register', kwargs={'activation_url': md5(str(request.COOKIES['sessionid']).encode('utf-8')).hexdigest()}))
        similar_users = get_object_or_none(models.User, email=email)
        if similar_users:
            raise ValueError('Пользователь с таким email уже существует')
        user = models.User.objects.create_user(email=email, password=password, username=None, avatar=avatar, name=fio, city=city, about=about)
        user.save()

        user = auth.authenticate(email=email, password=password)
        auth.login(request=request, user=user)


def forgot_password(request):
    pass


def change_password(request):
    pass


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('indexPage'))
        else:
            # print(form.errors)
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
    template_name = 'cabinet.html'

    def get_context_data(self, **kwards):
        context = super(UserCabinetChangeTemplate, self).get_context_data(**kwards)
        context['user'] = self.request.user

        return context
