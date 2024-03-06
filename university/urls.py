from django.urls import path
from .views import (
                    university_dashboard,)

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),

]
