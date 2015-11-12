from django import forms

class Username(forms.Form):
    username = forms.CharField(label = 'username', max_length = 20)
