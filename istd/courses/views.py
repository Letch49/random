from django.http import HttpResponseRedirect
from django.urls import reverse

from main.views import BaseView
from . import models


# Create your views here.

class CoursesView(BaseView):
    template_name = 'courses.html'

    def get_context_data(self, **kwards):
        context = super(CoursesView, self).get_context_data(**kwards)
        context['courses'] = models.Course.objects.all()
        context['categories'] = models.CourseCategory.objects.all()
        return context


class CourseView(BaseView):
    template_name = 'course.html'

    def get_context_data(self, **kwards):
        context = super(CourseView, self).get_context_data(**kwards)
        context['course'] = models.Course.objects.get(pk=kwards['pk'])
        context['isByu'] = models.SubscribeToCourse.objects.filter(user=self.request.user, course=context['course'])
        return context

    def post(self, request, *args, **kwargs):
        course = models.Course.objects.get(pk=request.POST['course'])
        user = models.UserProfile.objects.get(user=self.request.user)
        if user.balance - course.price < 0:
            raise ValueError('Недостаточно денег')
        user.balance = user.balance - course.price
        user.save()
        usersubcribe = models.SubscribeToCourse.objects.create(course=course, user=self.request.user)
        usersubcribe.save()
        return HttpResponseRedirect(reverse('bought'))


class CourseCategoryView(BaseView):
    template_name = 'courses.html'

    def get_context_data(self, **kwards):
        context = super(CourseCategoryView, self).get_context_data(**kwards)
        context['courses'] = models.Course.objects.filter(category_id=kwards['pk'])
        context['categories'] = models.CourseCategory.objects.all()
        return context


class BoughtView(BaseView):
    template_name = 'lk_bought.html'

    def get_context_data(self, **kwards):
        context = super(BoughtView, self).get_context_data(**kwards)
        context['bought'] = models.SubscribeToCourse.objects.filter(user=self.request.user)

        return context


class SearchCourseView(BaseView):
    template_name = 'courses.html'

    def get_context_data(self, **kwards):
        context = super(SearchCourseView, self).get_context_data(**kwards)
        search_query = self.request.GET['q']
        context['courses'] = models.Course.objects.filter(name__contains=search_query)
        context['categories'] = models.CourseCategory.objects.all()

        return context


def barter(request):
    message = request.POST['barter']

    return HttpResponseRedirect(reverse('barter'))
