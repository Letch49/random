"""istd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import IndexView
from courses import views as coursesView
from django.conf import settings
from django.conf.urls.static import static
from users.views import login, logout, register, UserCabinetChangeTemplate
from companies.views import CompaniesView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="indexPage"),
    path('courses/', coursesView.CoursesView.as_view(), name="courses"),
    path('courses/course-<int:pk>/', coursesView.CourseView.as_view(), name="course"),
    path('courses/category-<int:pk>/', coursesView.CourseCategoryView.as_view(), name="courses_category"),
    path('login/', login, name="login"),
    path('logout', logout, name="logout"),
    path('register/', register, name="register"),
    path('bought/', coursesView.BoughtView.as_view(), name="bought"),
    path('cabinet/', UserCabinetChangeTemplate.as_view(), name="cabinet"),
    path('companies/', CompaniesView.as_view(),name="companies"),
    path('search/', coursesView.SearchCourseView.as_view(), name="search"),
    path('barter/', coursesView.barter, name="barter"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
