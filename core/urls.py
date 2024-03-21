import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django_profiler import urls as profiler_urls
from django.urls import path, include

urlpatterns = [
    path('django/', admin.site.urls),  # admin site
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

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
# if settings.DEBUG:
#     urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
