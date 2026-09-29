from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GreetingForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def hello(request, name=None):
    # If no name was given, default to "stranger"
    if name is None:
        name = "stranger"
    return render(request, 'pages/hello.html', {'name': name})


def greet_form(request):
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            # Clean data
            name = form.cleaned_data['name']
            age = form.cleaned_data.get('age')
            # Redirect to a results page (or render directly)
            return render(request, 'pages/greet_result.html', {
                'name': name,
                'age': age,
            })
    else:
        form = GreetingForm()   # empty form for GET

    return render(request, 'pages/greet_form.html', {'form': form})
# Create your views here.
