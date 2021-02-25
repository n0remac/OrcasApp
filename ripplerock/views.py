from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post, Survey


class FrontPage(DetailView):
    template_name = 'ripplerock/home.html'

    def get(self, request, *args, **kwargs):
        surveys = Survey.objects.order_by('name')
        return render(request, self.template_name, {'surveys': surveys})


def ripplerock(request):
    about = Post.objects.filter(title__contains='about')
    contact = Post.objects.filter(title__contains='contact')
    return render(request, 'ripplerock/index.html', {"about": about, "contact": contact})
