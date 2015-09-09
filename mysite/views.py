'''
from django.shortcuts import render
from django.utils import timezone
from .models import Itmanual
from django.template import RequestContext
from django.shortcuts import render_to_response

    # posts = Itmanual.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def all_posts(request):
    context = RequestContext(request)
    # context_dict = {"post_title" :  }
    posts = Itmanual.objects.filter()
    # return render(request, 'it/post_list.html', {'posts': posts})
    return render(request, 'it/post_list.html', {'posts': posts})
'''
