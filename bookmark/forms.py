from django import forms
from .models import  Bookmark,Tags


class CreateBookmarkform(forms.ModelForm):
    class Meta:

        model = Bookmark
        fields =['name','url','tags','ispublic','tags']
        widgets = {

            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'url' :  forms.URLInput(attrs={'class':'form-control'}),
            'tags' : forms.SelectMultiple(attrs={'class':'form-control'})

        }
        labels ={
            'ispublic':'Public'

        }