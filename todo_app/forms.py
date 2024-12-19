from django import forms

from .models import TodoTask


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ["title"]
        widgets = {"completed": forms.RadioSelect}
