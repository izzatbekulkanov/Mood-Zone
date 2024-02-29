from django.urls import path
from .views import (post_dashboard)

urlpatterns = [
    path('', post_dashboard, name='post_dashboard'),

]
