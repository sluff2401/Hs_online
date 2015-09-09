#from . import views
from django.shortcuts                                 import render, render_to_response, get_object_or_404, redirect
from django.conf.urls                                 import include, url
from .models                                          import Itmanual, Language, Topic
from .forms                                           import PostForm

def all_items(request):
    #context = RequestContext(request)
    # context_dict = {"post_title" :  }
    posts = Itmanual.objects.filter()
    return render(request, 'it/post_list.html', {'posts': posts})
def language(request, language):
    posts = Itmanual.objects.filter(language=language)
    return render(request, 'it/post_list.html', {'posts': posts})
def topic(request, topic):
    posts = Itmanual.objects.filter(topic=topic)
    return render(request, 'it/post_list.html', {'posts': posts})
def single_item(request, language, topic):
    posts = Itmanual.objects.filter(language=language, topic=topic)
    return render(request, 'it/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Itmanual, pk=pk)
    return render(request, 'it/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'it/post_edit.html', {'form': form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('it.urls.post_detail', pk=post.pk)
        else:
            return render(request, 'it/post_edit.html', {'form': form})
    else:
        return render(request, 'it/debug.html', {})

def post_edit(request, pk):
    post = get_object_or_404(Itmanual, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('it.urls.post_detail', pk=post.pk)
        else:
            return render(request, 'it/post_edit.html', {'form': form})
    elif request.method == "GET":
        form = PostForm()
        return render(request, 'it/post_edit.html', {'form': form})
    else:
        return render(request, 'it/debug.html', {})

urlpatterns = [
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^(?P<language>[A-Z][a-z]*)/$', views.language),
    #url(r'^/(?P<topic>[A-Z][a-z]*)/$', views.topic),
    #url(r'^(?P<language>[A-Z][a-z]*)/(?P<topic>[A-Z][a-z]*)/$', views.item),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.all_posts),
    #url(r'^(?P<language>[A-Z][a-z]*)/$', language),
    #url(r'^it/(?P<language>[A-Z][a-z]*)/$', language),
    #url(r'^/(?P<topic>[A-Z][a-z]*)/$', topic),
    #url(r'^(?P<language>[A-Z][a-z]*)/(?P<topic>[A-Z][a-z]*)/$', single_item),
    #url(r'^(?P<language>[A-Z][a-z]*)/(?P<topic>[A-Z][a-z]*)/$', single_item),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    url(r'^$', all_items),
    url(r'^(?P<language>[A-Z][a-z]*)/$', language),
    url(r'^/(?P<topic>[A-Z][a-z]*)/$', topic),
    url(r'^(?P<language>[A-Z][a-z]*)/(?P<topic>[A-Z][a-z]*)/$', single_item),
]

