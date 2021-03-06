"""econvivial URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from main import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^consultation/', include('consultation.urls')),
    url(r'^assistance/', include('assistance.urls')),
    url(r'^conseil/', include('conseil.urls')),
    url(r'^planning/', include('planning.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^signout$', auth_views.logout,{'next_page': settings.LOGOUT_REDIRECT_URL}, name="signout"),
]+ static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'e-centreconvivial Administration'
admin.site.title = 'e-centreconvivial Administration'
