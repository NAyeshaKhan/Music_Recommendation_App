from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm , PlaylistCreateForm, AddSongToPlaylist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser, Playlist, Song  
from django.views.generic import ListView
from django.db.models import Q

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

class CustomUserView(viewsets.ModelViewSet): 
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializers 
   
def myform(request):
    if request.method=='POST':
        form=PredictionForm(request.POST or None)
        if form.is_valid():
            Age=request.user.age
            Gender=request.user.gender
            Mood=form.cleaned_data['mood']
            df=[[Age,Gender,Mood]]
            result = predict(df)
            result=result[0]
            song_list=Song.objects.filter(genre = result)
            return render(request, 'status.html', {"data": result,"songs":song_list}) 
            
    form=PredictionForm()
    return render(request, 'form.html', {'form':form})
    

def predict(df):
    try:
        dtree = joblib.load("C:/Users/User/Music_Recommendation_App/MusicApp/music_predict.joblib")
        y_pred = dtree.predict(df)
        newdf=pd.DataFrame(y_pred,columns=['Genre'])
        result=newdf["Genre"]
        return result
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def predict_api(request):
    data = request.query_params
    age= data.get('age')
    gender = data.get('gender')
    mood = data.get('mood')
    try:
        dtree = joblib.load("C:/Users/User/Music_Recommendation_App/MusicApp/music_predict.joblib")
        #predict using independent variables
        X=[[age,gender,mood]]
        y_pred = dtree.predict(X)
        newdf=pd.DataFrame(y_pred,columns=['Genre'])
        result=newdf["Genre"]
        return JsonResponse('Recommended genre is {}:'.format(newdf),safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

        
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

def addsongtoplaylist(request,id):
    if request.method == "GET":
        form = AddSongToPlaylist()
        form.fields["playlist"].queryset=Playlist.objects.filter(user=request.user)
        return render(request,'addsongtoplaylist.html',{'form':form})
    else:
        form = AddSongToPlaylist(request.POST)
        if form.is_valid():
            song=Song.objects.get(pk=id)
            song.playlist.set(form.cleaned_data.get('playlist'))
            return redirect('/playlist')

def playlistview(request,id):
    queryset = Song.objects.filter(playlist__pk=id)
    context = {
        "object_list": queryset
    }
    request.session['pid'] = id
    return render(request, "playlist_view.html", context)

def song_delete_playlist(request,sid):
    pid= request.session['pid']
    song = Song.objects.get(pk=sid)
    song.playlist.remove(pid)
    song.save()
    del request.session['pid']
    return playlistview(request,pid)

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