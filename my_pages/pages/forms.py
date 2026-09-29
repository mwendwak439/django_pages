
from django import forms


class GreetingForm(forms.Form):
    name = forms.CharField(
        label='Your name',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Sam',
            'class': 'form-control',
        })
    )
    age = forms.IntegerField(
        label='Your age',
        min_value=1,
        max_value=120,
        required=False,
    )