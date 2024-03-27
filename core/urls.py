import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from explorer import urls as explorer_url

urlpatterns = [
    path('django/', admin.site.urls),  # admin site
    path('user/', include('account.urls')),
    path('exam/', include('exam.urls')),
    path('', include('dashboard.urls')),
    path('library/', include('library.urls')),
    path('post/', include('post.urls')),
    path('admin/', include('authHemis.urls')),
    path('university/', include('university.urls')),
    path('explorer/', include('explorer.urls'))



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
