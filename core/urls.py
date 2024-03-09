from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django/', admin.site.urls),
    path('user/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('library/', include('library.urls')),
    path('post/', include('post.urls')),
    path('admin/', include('authHemis.urls')),
    path('university/', include('university.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
