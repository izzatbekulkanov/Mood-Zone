from django.urls import path
from mail.views import dashboard, emailCompose

app_name = 'mail'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('emailCompose', emailCompose, name='emailCompose')
]
