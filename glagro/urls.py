"""
URL configuration for glagro project.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('glagroapp.urls')),
]

# Serve media files during development and on Render
if settings.DEBUG or True:  # force serve even if DEBUG=False
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
