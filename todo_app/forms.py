from django import forms
from django.forms.widgets import PasswordInput

from .models import TodoTask


class LoginUser(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ["title"]
        widgets = {"completed": forms.RadioSelect}
