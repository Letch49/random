from . import models
from main.views import BaseView

# Create your views here.


class CompaniesView(BaseView):
    template_name = 'company.html'

    def get_context_data(self, **kwards):
        context = super(CompaniesView, self).get_context_data(**kwards)
        context['companies'] = models.Company.objects.all()
        return context
