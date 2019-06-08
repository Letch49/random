from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from ._models_proxy import UserProfile
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    username = models.CharField('username', max_length=50, null=True, blank=True)
    first_name = models.CharField('Имя пользователя', max_length=30, blank=True, null=True, default=None)
    date_joined = models.DateTimeField('дата регистрации', auto_now_add=True)
    is_staff = models.BooleanField('сотрудник?', default=False)
    is_confirm = models.BooleanField('подтверждённый юзер', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.email)
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=settings.EMAIL_HOST_USER, html_content="text/html", **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], html_content, **kwargs)

    # def get_user_profile(self):
    #     return UserProfile.objects.get(user__user=self.id)


class Profile(UserProfile):
    class Meta:
        verbose_name_plural = 'Профили пользователей'
        verbose_name = 'Профиль пользователя'
        proxy = True

    def __str__(self):
        return self.user


class BanList(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    reason = models.TextField('Причина бана')
    date_start = models.DateTimeField(auto_now_add=True, blank=True)
    date_end = models.DateTimeField(blank=True)

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Бан лист'
