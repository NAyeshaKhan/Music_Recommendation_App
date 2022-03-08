from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm , PlaylistCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser, Playlist, Song  

from .forms import PredictionForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser
from RecApp.serializer import CustomUserSerializers 
from sklearn.preprocessing import StandardScaler 
from rest_framework.views import APIView

import pickle
import joblib
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 

class CustomerUserView(viewsets.ModelViewSet): 
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializers 

def status(df):
    with open('C:/Users/User/Music_Recommendation_App/MusicApp/music_predict.sav' , 'rb') as f:
        model = pickle.load(f)
    X = df 
    y_pred = model.predict(X) 
    return y_pred
    
def FormView(request):
    if request.method=='POST':
        form=PredictionForm(request.POST or None)

        if form.is_valid():
            Age = form.cleaned_data['age']
            Gender = form.cleaned_data['gender']
            Mood = form.cleaned_data['mood']
            df=pd.DataFrame({'gender':[Gender], 'age':[Age], 'mood':[Mood]})
            df["gender"] = 1 if "Female" else 0
            result = status(df)
            songs= Song.objects.filter(genre=result)
            return render(request, 'status.html', {"genre": result,"rec":songs}) 
            
    form=PredictionForm()
    return render(request, 'form.html', {'form':form})


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

class SearchResultsView(ListView):
    model = Song
    template_name = 'search.html'

    def get_queryset(self):
        result = super(SearchResultsView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            object_list = Song.objects.filter(
                Q(title__icontains=query) | Q(genre__icontains=query) | Q(artist__icontains=query) | Q(
                    year__icontains=query))
            result = object_list
        else:
            result = None
        return result

