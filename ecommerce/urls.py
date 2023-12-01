from django.urls import path
from .views import (
    dashboard,
    categoriesListView,
    vendorDashboardView,
    shopMainView,
    wishlistView,
    userProfileView,
    productGridView,
    userListView,
    orderProcessView,
    invoiceView,
    productDetailView,
    productDetail3dView,
    productDetail360View
)

app_name = 'ecommerce'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categoriesList/', categoriesListView, name='categoriesList'),
    path('productGrid/', productGridView, name='productGrid'),
    path('productDetail/', productDetailView, name='productDetail'),
    path('productDetail3dView/', productDetail3dView, name='productDetail3d'),
    path('productDetail360View/', productDetail360View, name='productDetail360'),
    path('categoriesList/', categoriesListView, name='categoriesList'),
    path('vendorDashboard/', vendorDashboardView, name='vendorDashboard'),
    path('shopMain/', shopMainView, name='shopMain'),
    path('wishlist/', wishlistView, name='wishlist'),
    path('userProfile/', userProfileView, name='userProfile'),
    path('userList/', userListView, name='userList'),
    path('orderProcess/', orderProcessView, name='orderProcess'),
    path('invoice/', invoiceView, name='invoice'),
]
