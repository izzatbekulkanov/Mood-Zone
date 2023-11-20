from django.urls import path
from .views import mainView, dashboardView, customerView, friendView, whishlistView

urlpatterns = [
    path('', mainView, name='mainView'),
    path('home/', dashboardView, name='dashboardView'),
    path('customer/', customerView, name='customerView'),
    path('friend/', friendView, name='friendView'),
    path('whishlist/', whishlistView, name='whishlistView'),
]