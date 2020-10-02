from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print("clear")
        if form.is_valid():
            print("Validation Successful")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'user/profile.html')
