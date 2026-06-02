from django import forms
from .models import tweet

class tweetForm(forms.ModelForm):
    class meta:
        model = tweet
        fields = ['text','photo'] 