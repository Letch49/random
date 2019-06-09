import datetime

from django.db.models import Count
from django.views.generic import TemplateView

from courses.models import SubscribeToCourse, Course
from . import models as modelsAdmin


# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwards):
        context = super(BaseView, self).get_context_data(**kwards)
        if self.request.session.session_key is None:
            self.request.session.create()
        context['main'] = modelsAdmin.AdminModel

        return context


class IndexView(BaseView):
    template_name = 'index.html'

    def get_context_data(self, **kwards):
        context = super(IndexView, self).get_context_data(**kwards)
        context['popular'] = SubscribeToCourse.objects.values('course', 'course__name', 'course__description', 'course__price', 'course__img', 'course__category__name').annotate(
            total=Count('course')).order_by('-total')[:6]
        context['popular_categories'] = SubscribeToCourse.objects.values('course__category__name', 'course__category_id').annotate(
            total=Count('course__category__name', distinct=True)).order_by('total')[:6]
        context['afisha'] = Course.objects.distinct().filter(date_start__gte=(datetime.datetime.now() - datetime.timedelta(days=7)), price=0)
        context['afisha_count'] = context['afisha'].count()
        return context
