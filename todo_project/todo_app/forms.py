from django import forms
from .models import Todos

class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields= ["title","description","finished","date","deadline"]
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }