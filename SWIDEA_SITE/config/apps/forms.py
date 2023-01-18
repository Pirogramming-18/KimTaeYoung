from django import forms
from .models import Idea, devTool

class ideaForm(forms.ModelForm):
    
    class Meta:
        model = Idea
        fields = ['image', 'name', 'content', 'dev_tool', 'interest_degree']
    
    


class toolForm(forms.ModelForm):
  class Meta:
    model = devTool
    fields = ['name', 'content', 'classification',]