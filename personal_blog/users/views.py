from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .form import UserRegisterForm, UpdateProfileForm, UserUpdateForm
from django.contrib.auth.models import User
from .models import Profile
import logging


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            logging.debug('Form is valid')

            return redirect('login')

        else:
            logging.error('Form Invalid')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST
                                   , request.FILES
                                   , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm()

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context=context)

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST, next='blog-home')
#         if form.confirm_login_allowed(form):
#             return redirect('blog-home')
#         else:
#             return redirect('blog-about')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {form: form})

