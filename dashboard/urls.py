from django.urls import path
from .views import dashboardView, adminPage, blankPage, userView, inboxView, \
    iconSolidView, iconOutlineView, iconDualToneView, apiControlView, apiCustomerView, \
    apiUniversityView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('admin-page/', adminPage, name='adminPage'),
    path('blank-page/', blankPage, name='blankPage'),
    path('user/', userView, name='userView'),
    path('inbox/', inboxView, name='inboxView'),
    path('iconSolid/', iconSolidView, name='iconSolid'),
    path('iconOutline/', iconOutlineView, name='iconOutline'),
    path('iconDual/', iconDualToneView, name='iconDualTone'),
    path('apiControl/', apiControlView, name='apiControl'),
    path('apiCustomer/', apiCustomerView, name='apiCustomer'),
    path('apiUniversity/', apiUniversityView, name='apiUniversity')
]
