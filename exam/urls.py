from django.urls import path
from exam.views import exam_dashboard

urlpatterns = [
    path('', exam_dashboard, name='exam_dashboard'),
    # path('weather', weather, name='weather'),
]