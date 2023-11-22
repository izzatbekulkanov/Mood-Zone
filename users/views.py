from django.shortcuts import render
from .models import CustomUser

# Create your views here.


def usersListView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/app/user-list.html', context)
