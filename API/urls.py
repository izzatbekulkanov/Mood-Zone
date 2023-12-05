from django.urls import path
from .views import apiControlView, apiCustomerView, \
    apiUniversityView

app_name = 'API'

urlpatterns = [
    path('apiControl/', apiControlView, name='apiControl'),
    path('apiCustomer/', apiCustomerView, name='apiCustomer'),
    path('apiUniversity/', apiUniversityView, name='apiUniversity')
]