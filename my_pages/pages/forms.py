
from django import forms
from .models import Greeting



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

class GuestbookEntryForm(forms.ModelForm):
 class Meta:
        model = Greeting
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Leave a message...',
                'rows': 4,
                'class': 'form-input',
            }),
        }
        labels = {
            'name': 'Your name',
            'message': 'Your message',
        }