from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField('Возраст пользователя', blank=True, null=True)
    city = models.CharField('Город', max_length=100, blank=True, null=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True, null=True)
    about = models.TextField('О себе', blank=True, null=True)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1)
    balance = models.PositiveSmallIntegerField('Баланс', default=0)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'
