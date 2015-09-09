from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

def person_list(request):
    persons = Person.objects.all().order_by('second_name')
    return render(request, 'contacts/person_list.html', {'persons': persons})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contacts/person_detail.html', {'person': person})

@login_required
def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.author = request.user
            person.published_date = timezone.now()
            person.save()
            return redirect('contacts.views.person_list')
    else:
        form = PersonForm()
    return render(request, 'contacts/person_edit.html', {'form': form})

@login_required
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.author = request.user
            person.published_date = timezone.now()
            person.save()
            return redirect('contacts.views.person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'contacts/person_edit.html', {'form': form})

@login_required
def person_remove(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('contacts.views.person_list')