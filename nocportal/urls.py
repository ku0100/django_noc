"""nocportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', include('homepage.urls')),
    url(r'^network_resources/', include('network_resources.urls', namespace='network_resources')),
    url(r'^device_categories/', include('device_categories.urls', namespace='device_categories')),
    url(r'^device_inventory/', include('device_inventory.urls', namespace='device_inventory')),
    url(r'^on_call/', include('on_call.urls', namespace='on_call')),
    url(r'^contact_info/', include('contact_info.urls', namespace='contact_info')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)