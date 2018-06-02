from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="planning"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<plan>[-\w]+)/$',
        views.plan_detail,
        name='plan_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<username>[-\w]+)/$',
        views.plan_exchange,
        name='plan_exchange'),
]
