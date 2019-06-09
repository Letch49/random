from django.conf import settings
from django.db import models

# Create your models here.
from companies.models import Company
from users.models import UserProfile


class Tags(models.Model):
    name = models.CharField('Имя Тега', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'


class CourseCategory(models.Model):
    name = models.CharField('Название категории курса', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория курса'


class Course(models.Model):
    name = models.CharField('Название курса', max_length=100)
    price = models.IntegerField('Цена')
    duration = models.IntegerField('Длительность')
    description = models.TextField('Описание')
    img = models.ImageField('Изображение курса', upload_to="courses/", null=True, blank=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT)
    date_start = models.DateTimeField('Дата и время начала курса', auto_now=True, blank=True)
    # TODO: ADD type
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    company_id = models.ForeignKey(Company, max_length=20, blank=True, null=True, on_delete=models.SET_NULL)  # TODO: создать модель компании

    def __str__(self):
        return str(self.name)

    def get_pk(self):
        return self.objects.get(name=self.name)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class TagsToCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT)

    def __str__(self):
        return '{course} + {tag}'

    class Meta:
        verbose_name = 'Тег к курсу'


class Lesson(models.Model):
    name = models.CharField('Название урока', max_length=255)
    video = models.URLField('Видеоурок', null=True, blank=True)
    text = models.TextField('Текст урока', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class FilesForLesson(models.Model):
    name = models.CharField('Название файла', max_length=255)
    file = models.FileField('Файл', upload_to='lesson/')

    def __str__(self):
        return self.name


class FilesToLesson(models.Model):
    file = models.ForeignKey(FilesForLesson, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.lesson)

    class Meta:
        verbose_name = 'Файл для урока'


class LessonToCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.course.name)

    class Meta:
        verbose_name = 'Урок к курсу'


class Package(models.Model):
    name = models.CharField('Название пакета', max_length=255)
    description = models.TextField('Описание профессии')
    img = models.ImageField('Изображение профессии', upload_to='courses/professions/', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пакет курсов'


class CoursesInPackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.package.name)

    class Meta:
        verbose_name = 'Курс в пакете'
        verbose_name_plural = 'Курсы в пакете'


class SubscribeToCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.course)

    def get_courses(self, user):
        return self.course.objects.filter(user=user)

    class Meta:
        verbose_name = 'Запись на курс'
