from django import forms
from .models import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'name_in_esg', 'email', 'phone_a', 'phone_b')