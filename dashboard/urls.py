from django.urls import path
from .views import mainView, blankPage, adminView, alernative_dashboard, whishlistView, userView, inboxView

urlpatterns = [
    path('', mainView, name='mainView'),
    path('blankPage/', blankPage, name='blankPage'),
    path('adminView/', adminView, name='adminView'),
    path('alernative/', alernative_dashboard, name='alernative'),
    path('whishlist/', whishlistView, name='whishlistView'),
    path('user/', userView, name='userView'),
    path('inbox/', inboxView, name='inboxView'),
]