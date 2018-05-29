from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="consultation"),
    url(r'^new_consultation$', views.new_consultation, name="new_consultation"),
    url(r'^(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<consultation>[-\w]+)/$',views.consultation_detail,name='consultation_detail'),
]
