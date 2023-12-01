from django.urls import path
from .views import (dashboard, categoriesListView, vendorDashboardView, shopMainView, wishlistView, )
app_name = 'ecommerce'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categoriesList/', categoriesListView, name='categoriesList'),
    path('vendorDashboard/', vendorDashboardView, name='vendorDashboard'),
    path('shopMain/', shopMainView, name='shopMain'),
    path('wishlist/', wishlistView, name='wishlist'),
    path('userProfile/', userProfileView, name='userProfile'),
]
