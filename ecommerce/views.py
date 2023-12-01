from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'e-commerce/dashboard/main.html')
def categoriesListView(request):
    return render(request, 'e-commerce/categories-list.html')
def vendorDashboardView(request):
    return render(request, 'e-commerce/vendor-dashboard.html')
def shopMainView(request):
    return render(request, 'e-commerce/shop-main.html')
def wishlistView(request):
    return render(request, 'e-commerce/wishlist.html')
def userProfileView(request):
    return render(request, 'e-commerce/user-profile.html')