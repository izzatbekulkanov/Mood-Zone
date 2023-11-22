from django.shortcuts import render


# Create your views here.
def mainView(request):
    return render(request, 'base/index.html')
def blankPage(request):
    return render(request, 'base/blank-page.html')
def adminView(request):
    return render(request, 'base/admin.html')
def alernative_dashboard(request):
    return render(request, 'base/alternate-dashboard.html')
def whishlistView(request):
    return render(request, 'home/whishlist.html')
def userView(request):
    return render(request, 'home/users.html')
def inboxView(request):
    return render(request, 'email/inbox.html')
