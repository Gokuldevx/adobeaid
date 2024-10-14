
from django import forms
from home_app.models import sermodel

class serform(forms.Form):
    
    sname=forms.CharField(max_length=100)
    simg=forms.FileField()
    class Meta:
        model=sermodel
        fields=['spid','sname','desc','simg']