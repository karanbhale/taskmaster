from django import forms
from .models import tasks

class tasklist(forms.ModelForm):
    
    class Meta:
        model = tasks
        fields = ["task","done"]
        



