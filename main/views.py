from django.shortcuts import render


# Create your views here.
def mainView(request):
    return render(request, 'base/main.html')
def dashboardView(request):
    return render(request, 'home/dashboard.html')
def customerView(request):
    return render(request, 'home/customer.html')
def friendView(request):
    return render(request, 'home/friend.html')
def whishlistView(request):
    return render(request, 'home/whishlist.html')
