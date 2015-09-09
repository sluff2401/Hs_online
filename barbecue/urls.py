from django.shortcuts                                 import render
from django.conf.urls                                 import url
#from django.http                                      import HttpResponse

def accounts(request):
    return render(request, 'barbecue/base.html')
    #return HttpResponse("Hello, world.")

urlpatterns = [
    url(r'^$', accounts),
]








