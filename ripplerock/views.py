from django.shortcuts import render
from django.views.generic import DetailView
from .models import Paragraph, Survey
from django.core.paginator import Paginator


class SurveyView(DetailView):
    template_name = 'ripplerock/survey.html'

    def get(self, request, *args, **kwargs):
        surveys = Survey.objects.order_by('age')
        paginator = Paginator(surveys, 1)
        page = request.GET.get("page")
        results = paginator.get_page(page)

        return render(request, self.template_name, {'surveys': results})


class Home(DetailView):
    template_name = 'ripplerock/home.html'

    def get(self, request, *args, **kwargs):
        about = Paragraph.objects.filter(page='home')

        return render(request, self.template_name, {'about': about})


class Mission(DetailView):
    template_name = 'ripplerock/mission.html'

    def get(self, request, *args, **kwargs):
        about = Paragraph.objects.filter(page='mission')

        return render(request, self.template_name, {'about': about})
