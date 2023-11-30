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
def iconSolidView(request):
    return render(request, 'dashboard/icons/solid.html')
def iconOutlineView(request):
    return render(request, 'dashboard/icons/outline.html')
def iconDualToneView(request):
    return render(request, 'dashboard/icons/dual-tone.html')
