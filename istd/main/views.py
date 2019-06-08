from django.views.generic import TemplateView

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
    template_name = 'base.html'

    def get_context_data(self, **kwards):
        context = super(IndexView, self).get_context_data(**kwards)
        context['lol'] = 1

        return context
