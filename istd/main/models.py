from django.db import models


# Create your models here.
class AdminModel(models.Model):
    title = models.CharField(max_length=255)
    logo = models.FileField('Логотип', upload_to='main/')
    meta_keywords = models.TextField('Ключевые слова')
    description = models.TextField('Описание (поисковик)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основные настройки сайта'
