
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('library/', include('library.urls')),
    path('post/', include('post.urls')),
    path('university/', include('university.urls')),
]
