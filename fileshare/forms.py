from django import forms
from django.forms import ModelForm
from .models import *



class AddForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_posted','author']
        widgets = {
            
            'title':forms.TextInput(attrs={'class' : 'account-input' }),
            'content':forms.Textarea(attrs={'class': 'textarea-input '}),
            
            
            
            }
        
