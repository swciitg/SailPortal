"""SAIL_SITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sail/admin/', admin.site.urls),
    path('sail/accounts/', include('allauth.urls')),
    path('sail/opportunity/', include('opportunity.urls')),
    path('sail/', include('home.urls')),
    path('sail/blog/', include('blog.urls')),
    path('sail/events/', include('events.urls')),
    path('sail/initiatives/', include('initiatives.urls')),
    path('sail/services', include('services.urls')),
    path('sail/team/', include('team.urls')),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
