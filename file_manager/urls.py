from django.urls import path
from .views import dashboard, allFiles, documentFolder, imageFolder, trash, videoFolder
app_name = 'file_manager'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('allFiles/', allFiles, name='allFiles'),
    path('documentFolder/', documentFolder, name='documentFolder'),
    path('imageFolder/', imageFolder, name='imageFolder'),
    path('trash/', trash, name='trash'),
    path('videoFolder/', videoFolder, name='videoFolder'),
]
