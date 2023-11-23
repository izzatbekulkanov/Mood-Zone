from django.shortcuts import render


# Create your views here.
def dashboardView(request):
    return render(request, 'dashboard/main.html')
def adminPage(request):
    return render(request, 'dashboard/admin.html')
def blankPage(request):
    return render(request, 'dashboard/blank-page.html')

def userView(request):
    return render(request, 'home/users.html')
def inboxView(request):
    return render(request, 'email/inbox.html')
