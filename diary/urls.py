from django.conf             import settings
from django.conf.urls.static import static
from django.conf.urls        import url
from .                       import views

from django.shortcuts                                 import render
from django.conf.urls                                 import url

urlpatterns = [
    url(r'^$',                             views.events_hardcoded,  name='events_hardcoded'),
    #url(r'^$',                             views.event_list,       name='event_list'),
    #url(r'^event/(?P<pk>[0-9]+)/$',         views.event_detail,     name='event_detail'),
    url(r'^event/new/$',                    views.event_new,        name='event_new'),
    url(r'^event/(?P<pk>[0-9]+)/edit/$',    views.event_edit,       name='event_edit'),
    url(r'^event/(?P<pk>[0-9]+)/remove/$',  views.event_remove,     name='event_remove'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
