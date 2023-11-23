from django.urls import path
from .views import (
    landingPageView
)
app_name = 'landing_page'

urlpatterns = [
    path('', landingPageView, name='landingPage'),
]
