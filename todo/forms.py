from django import forms
from .models import TodoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ('title', 'memo', 'priority', 'duedate')

        labels = {
            'priority': '重要度'
        }

        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "タイトル"}),
            'memo': forms.Textarea(attrs={"placeholder": "メモ"}),
            'duedate': forms.DateInput(attrs={"type": "date"}),
            'priority': forms.RadioSelect(attrs={"type": "radio", "class": "radio"})
        }