from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Tags)
class Tags(admin.ModelAdmin):
    list_display = ('name',)


class FilesTabular(admin.TabularInline):
    model = models.FilesToLesson


@admin.register(models.Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ['id']
    inlines = [FilesTabular]


@admin.register(models.SubscribeToCourse)
class SubscribeToCourse(admin.ModelAdmin):
    list_display = ['course', 'user']


class LessonsTabular(admin.TabularInline):
    model = models.LessonToCourse


class TagsTabular(admin.TabularInline):
    model = models.TagsToCourse


@admin.register(models.CourseCategory)
class CourseCategory(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    inlines = [LessonsTabular, TagsTabular]


class CourseInPackageTabular(admin.TabularInline):
    model = models.CoursesInPackage


@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [CourseInPackageTabular]
