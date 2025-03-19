from django import forms
from django.contrib.auth import get_user_model
from .models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter task name"})
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Enter task description"})
    )
    deadline = forms.DateTimeField(
        label="",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=""
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type', 'priority', 'deadline', 'assignees']
        labels = {
            'task_type': '',
            'priority': '',
        }
