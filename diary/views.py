from django.shortcuts                     import render, get_object_or_404, redirect
from django.utils                         import timezone
from django.contrib.auth.decorators       import login_required
from django.contrib.auth.models           import User
from .models                              import Event
from .forms                               import EventForm


def events_hardcoded(request):
    return render(request, 'diary/base_hardcoded.html', {})

def event_list(request):
    events = Event.objects.filter(status=True).order_by('event_date')
    return render(request, 'diary/event_list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'diary/event_detail.html', {'event': event})

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            event.author_name = user.username
            event.author = request.user
            event.save()
            return redirect('diary.views.event_list')
    else:
        form = EventForm()
    return render(request, 'diary/event_edit.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            event.author_name = user.username
            event.author = request.user
            event.save()
            return redirect('diary.views.event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'diary/event_edit.html', {'form': form})

@login_required
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('diary.views.event_list')
