from django.shortcuts import render
from django.contrib.auth import get_user_model



def threejs(request):
    User = get_user_model()
    data = {}
    users = User.objects.all()
    for user in users:
        print('==================')
        print(user.id)
        data.update({user.id: user.username})
    return render(request, 'graph/threejs.html', {'users': data})