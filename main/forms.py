from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'
        widgets = {
            'Content': forms.Textarea(attrs={'class':'post', 'placeholder':"what's new?", "style":"height:100px;"}),
        }
        labels = {
            'user': (''),
            'Content': (''),
        }
        