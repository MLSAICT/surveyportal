# survey_portal/survey_portal/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surveyor/', include('surveyor.urls', namespace='surveyor')),
    path('admin_panel/', include('admin_panel.urls', namespace='admin_panel')),
    path('surveyor/', include('surveyor.urls', namespace='surveyor')),
    path('__reload__/', include('django_browser_reload.urls')),

    # Add other paths as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)