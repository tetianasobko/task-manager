from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Task, Worker


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter task name"})
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"rows": 5, "placeholder": "Enter task description"})
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
        fields = [
            "name",
            "description",
            "task_type",
            "priority",
            "deadline",
            "assignees"
        ]
        labels = {
            "task_type": "",
            "priority": "",
        }


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class WorkerCreateForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter first name"})
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter last name"})
    )
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter username"})
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "Enter email"})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )

        labels = {
            "position": ""
        }


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["position"]

        labels = {
            "position": ""
        }
