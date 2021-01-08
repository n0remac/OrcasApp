from django.shortcuts import render
from .models import Post

def ripplerock(request):
    print('=================')
    about = Post.objects.filter(title__contains='about')
    contact = Post.objects.filter(title__contains='contact')
    return render(request, 'ripplerock/index.html', {"about": about, "contact": contact})
