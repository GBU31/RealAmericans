from django import forms
from .models import *

class pfpForm(forms.ModelForm):
    class Meta:
        model = profilePic
        fields = ['pic']



class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['Content']
        widgets = {
            'Content': forms.Textarea(attrs={'class':'post', 'placeholder':"what's new?", "style":"height:100px;"}),
        }
        labels = {
            'user': (''),
            'Content': (''),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['Comment']
        widgets = {
            'Comment': forms.Textarea(attrs={'class':'post', "style":"height:100px;"}),
        }
        labels = {
            'user': (''),
            'to_pk': (''),
            'Comment':(''),
        }


    