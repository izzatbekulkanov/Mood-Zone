from django.shortcuts import render

# Create your views here.

def mainView(request):
    return render(request, 'partials/base.html')
def studentView(request):
    return render(request, 'users/students.html')
