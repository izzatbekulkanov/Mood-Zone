from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('landing-page/', include('landing_page.urls')),
    path('social/', include('social.urls')),
    path('mail/', include('mail.urls')),
    path('ecommerce/', include('ecommerce.urls')),
    path('appointment/', include('appointment.urls')),
    path('blog/', include('blog.urls')),
    path('file-manager/', include('file_manager.urls')),
    path('chat/', include('chat.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
