from django.conf import settings
from django.db import models

from companies import models as companies_models
from courses import models as courses_models


# Create your models here.

class Comments(models.Model):
    text = models.TextField('Комментарий')
    date_add = models.DateTimeField('Дата добавления комментария', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class CommentsTo(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    isLesson = models.ForeignKey(courses_models.Lesson, null=True, blank=True, on_delete=models.PROTECT)
    isCourse = models.ForeignKey(courses_models.Course, null=True, blank=True, on_delete=models.PROTECT)
    isPackage = models.ForeignKey(courses_models.Package, null=True, blank=True, on_delete=models.PROTECT)
    isUser = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)
    isCompany = models.ForeignKey(companies_models.Company, null=True, blank=True, on_delete=models.PROTECT)
    id_of_target = models.IntegerField('id таргетированной модели', db_index=True)

    def __str__(self):
        return str(self.comment.user)

    class Meta:
        verbose_name = 'Коменатрий к таргету'
        verbose_name_plural = 'Коментарии к таргету'


class Likes(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.PROTECT)
    like = models.IntegerField('Лайк')
    isLesson = models.ForeignKey(courses_models.Lesson, null=True, blank=True, on_delete=models.PROTECT)
    isCourse = models.ForeignKey(courses_models.Course, null=True, blank=True, on_delete=models.PROTECT)
    isPackage = models.ForeignKey(courses_models.Package, null=True, blank=True, on_delete=models.PROTECT)
    isUser = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)
    isCompany = models.ForeignKey(companies_models.Company, null=True, blank=True, on_delete=models.PROTECT)
    id_of_target = models.IntegerField('id таргетированной модели', db_index=True)

    def __str__(self):
        return str(self.user)

    def like(self, user, modelId):
        obj, liked = self.objects.get_or_create(user=user, id_of_target=modelId)
        if not liked:
            obj.delete()
        return obj.liked

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
