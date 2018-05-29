from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="assistance"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<assistance>[-\w]+)/$',views.assistance_detail,name='assistance_detail'),
]
    
