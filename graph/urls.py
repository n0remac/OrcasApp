from django.urls import path
from . import views

urlpatterns = [
    path('', views.threejs, name='threejs'),
]