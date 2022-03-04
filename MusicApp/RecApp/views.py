from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser, Playlist  


def register_request(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			#messages.success(request, "Registration successful." )
			return redirect(reverse("RecApp:dashboard"))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserCreationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

  
     
def home(request):
    return render(request, 'home.html')


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return redirect(reverse("RecApp:dashboard"))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	#messages.info(request, "You have successfully logged out.") 
	return redirect("RecApp:home")


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def playlist_read(request):
    playlist={}
    playlist["data"]=Playlist.objects.filter(user=request.user)
    
    return render(request, 'playlist_read.html', playlist)