from django import forms
from .models import Itmanual
class PostForm(forms.ModelForm):
    class Meta:
        model = Itmanual
        fields = ( 'language', 'topic', 'text',)
