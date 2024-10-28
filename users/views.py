from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def register(request):
    """New user registration."""
    if request.method == 'GET':
        # Show blank registrattion form
        form = UserCreationForm()
    elif request.method == 'POST':
        form = UserCreationForm(data = request.POST)
    
    if form.is_valid():
        new_user = form.save()
        # Log the new user in and redirect to home page
        login(request, new_user)
        return redirect('HAM_logger:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
