from django import forms
from .models import *

class pfpForm(forms.ModelForm):
    class Meta:
        model = profilePic
        fields = ['pic']
        widgets = {
            'pic': forms.TextInput(attrs={'placeholder':"url"}),
        }
        labels = {
            'pic':''
        }



class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['Content']
        widgets = {
            'Content': forms.TextInput(attrs={'class':'post', 'placeholder':"what's new?", "style":"height:100px;"}),
        }
        labels = {
            'user': '',
            'Content': '',
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['Content']
        widgets = {
            'Content': forms.TextInput(attrs={'class':'post', "style":"height:100px;"}),
        }
        labels = {
            'user': '',
            'to_pk': '',
            'Content':'',
        }


    