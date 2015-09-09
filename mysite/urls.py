from django.shortcuts                                 import render
from django.conf.urls                                 import include, url
from django.contrib                                   import admin

def home_page(request):
    return render(request, 'mysite/base.html', {})

urlpatterns = [
    url(r'^$',                 'mysite.urls.home_page'),
    url(r'admin/',             include(admin.site.urls)),
    url(r'^admin/',            include(admin.site.urls)),
    url(r'^accounts/login/$',  'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    #url(r'^accounts/profile/$',  'django.contrib.auth.views.profile'),
    url(r'it/',                include('it.urls')),
    url(r'djgtut/',            include('djgtut.urls')),
    url(r'barbecue/',          include('barbecue.urls')),
    url(r'contacts/',          include('contacts.urls')),
]
