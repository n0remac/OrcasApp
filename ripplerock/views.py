from django.shortcuts import render

def ripplerock(request):
    return render(request, 'ripplerock/index.html', {})