from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="consultations"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<consultation>[-\w]+)/$',views.consultation_detail,name='consultation_detail'),
]
