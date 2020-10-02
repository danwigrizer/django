from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.models import User
import logging

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            logging.debug('Form is valid')

            return redirect('blog-home')

        else:
            logging.error('Form Invalid')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
