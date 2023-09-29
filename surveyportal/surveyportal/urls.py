"""
URL configuration for surveyportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import user.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.index, name='index'),
    path('login/', user.views.login_user, name='login'),
    path('userdashboard/', user.views.userdashboard, name='userdashboard'),
    path('psmrequests/', user.views.psmrequests, name='psmrequests'),
    path('usersettings/', user.views.usersettings, name='usersettings'),
    path('__reload__/', include('django_browser_reload.urls')),
    # path('view-letter/<path:file_path>/', view_letter, name='view_letter'),
    # path('view-document/<str:model>/<int:pk>/', view_uploaded_document, name='view_document'),
    path('view-document/<str:model>/<int:pk>/', user.views.view_uploaded_document, name='view_document'),
    path('beyrah/', user.views.beyrah, name='beyrah'),
    path('psm_request/<int:pk>/', user.views.psm_request_detail, name='psm_request_detail'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)