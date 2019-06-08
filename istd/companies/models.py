from django.conf import settings
from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField('Название компании', max_length=150)
    description = models.TextField('Описание')
    img = models.ImageField('Картинка компании', upload_to='companies/', null=True, blank=True)
    date_created = models.DateField('Дата создания', blank=True, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class UsersInCompanies(models.Model):
    ROLE_CHOICES = [
        (1, 'admin'),
        (2, 'moderator'),
        (3, 'member')
    ]
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default='3')

    def __str__(self):
        return str(self.company.name)
