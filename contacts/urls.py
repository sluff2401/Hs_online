from django.conf             import settings
from django.conf.urls.static import static
from django.conf.urls        import url
from .                       import views

urlpatterns = [
    url(r'^$',                             views.person_list,       name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$',         views.person_detail,     name='person_detail'),
    url(r'^person/new/$',                    views.person_new,        name='person_new'),
    url(r'^person/(?P<pk>[0-9]+)/edit/$',    views.person_edit,       name='person_edit'),
    url(r'^person/(?P<pk>[0-9]+)/remove/$',  views.person_remove,     name='person_remove'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

