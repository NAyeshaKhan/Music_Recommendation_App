import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm , PlaylistCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser, Playlist  


class Prediction(APIView):
    def post(self, request):
        #data = request.data
        age= request.GET.get('Age')
        gender = request.GET.get('Gender')
        mood = request.GET.get('Mood')
        dtree = ApiConfig.model
        
        #predict using independent variables
        PredictionMade = dtree.predict([[age, gender, mood]])
        response_dict = {"Recommended Genre": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)


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
    return render(request, 'playlist_read.html')

def playlist_create(request):
	if request.method == "GET":
		form = PlaylistCreateForm()
		return render(request,'playlist_create.html',{'form':form})
	else:
		form = PlaylistCreateForm(request.POST)
		if form.is_valid():
			playlist=form.save(commit=False)
			playlist.user = request.user
			playlist.save()
			return redirect('/playlist')

def playlist_delete(request,id):
	playlist = Playlist.objects.get(pk=id)
	playlist.delete()
	return redirect('/playlist')
