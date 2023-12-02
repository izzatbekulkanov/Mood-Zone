from django.urls import path
from .views import (dashboard, bookAppointmentView, doctorVisitView, )
app_name = 'appointment'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('bookAppointment', bookAppointmentView, name='bookAppointment'),
    path('doctorVisit', doctorVisitView, name='doctorVisit'),
]
