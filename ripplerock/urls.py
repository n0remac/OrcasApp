from django.urls import path
from .views import SurveyView, Home, Mission

urlpatterns = [
    #path('', views.ripplerock, name='ripplerock'),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('', Home.as_view(), name='home'),
    path('mission/', Mission.as_view(), name='mission'),
]