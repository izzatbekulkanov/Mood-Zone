from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'e-commerce/dashboard/main.html')
def categoriesListView(request):
    return render(request, 'e-commerce/categories-list.html')
def productGridView(request):
    return render(request, 'e-commerce/products3632.html')
def vendorDashboardView(request):
    return render(request, 'e-commerce/vendor-dashboard.html')
def shopMainView(request):
    return render(request, 'e-commerce/shop-main.html')
def wishlistView(request):
    return render(request, 'e-commerce/wishlist.html')
def userProfileView(request):
    return render(request, 'e-commerce/user-profile.html')
def userListView(request):
    return render(request, 'e-commerce/user-list.html')
def orderProcessView(request):
    return render(request, 'e-commerce/order-process.html')
def invoiceView(request):
    return render(request, 'e-commerce/invoice.html')
def productDetailView(request):
    return render(request, 'e-commerce/product-detail.html')
def productDetail3dView(request):
    return render(request, 'e-commerce/product-detail-3d.html')
def productDetail360View(request):
    return render(request, 'e-commerce/product-detail-360.html')