from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def signup(request):
    if request.method == "GET":
        return render(
            request, "signup.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #email = form.cleaned_data.get('email')
            #password = form.cleaned_data.get('password1')
            login(request, user)
            return redirect("RecApp:dashboard")
          
     
def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if user is not None:
                login(request, user)
                return redirect("RecApp:dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
