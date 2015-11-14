from django import forms
from .models import To_do
class Username(forms.Form):
    username = forms.CharField(label = 'username', max_length = 20)

class AddTodo(forms.ModelForm):
    class Meta:
        model = To_do
        fields = ['priority', 'description']
