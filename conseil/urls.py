from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="conseil"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    ]
