from django import forms
from .models import Note

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','description']


class NoteUpdationForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','description']