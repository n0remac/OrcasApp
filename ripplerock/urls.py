from django.urls import path
from .views import FrontPage

urlpatterns = [
    #path('', views.ripplerock, name='ripplerock'),
    path('', FrontPage.as_view(), name='frontpage'),
]