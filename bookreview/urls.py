from django.conf.urls import url
from . import views

urlpatterns = [
    # /bookreview/
    url(r'^$', views.index, name='index'),

    #/bookreview/id/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
