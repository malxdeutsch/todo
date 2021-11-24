from django import forms
from .models import Category

class TodoForm(forms.Form):
    title = forms.CharField(max_length=200)
    details = forms.CharField(max_length=200)
    has_been_done= forms.BooleanField()
    date_completion = forms.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    deadline_date = forms.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    category= forms.ModelChoiceField(queryset=Category.objects.all())
