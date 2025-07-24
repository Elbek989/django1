from django.core.exceptions import ValidationError
from django import forms
from .models import *
class NewsForm(forms.Form):
    title=forms.CharField(max_length=150, label='News',
                          widget=forms.TextIput(attrs={"class":"form-control"}))
    context=forms.CharField(label='Text',required=False, widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    is_bool=forms.BooleanField(label='is bool', initial=True)
    category=forms

