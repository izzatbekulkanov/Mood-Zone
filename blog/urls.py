from django.urls import path
from .views import dashboard, blogMain, blogCategory, blogComments, blogGrid, blogList, blogDetail, blogTrending
app_name = 'blog'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('blogMain/', blogMain, name='blogMain'),
    path('blogCategory/', blogCategory, name='blogCategory'),
    path('blogComments/', blogComments, name='blogComments'),
    path('blogGrid/', blogGrid, name='blogGrid'),
    path('blogList/', blogList, name='blogList'),
    path('blogDetail/', blogDetail, name='blogDetail'),
    path('blogTrending/', blogTrending, name='blogTrending'),

]
