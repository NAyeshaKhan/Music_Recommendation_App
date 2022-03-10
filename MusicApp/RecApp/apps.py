import os
import joblib
from django.apps import AppConfig
from django.conf import settings
import joblib

class RecAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RecApp'

class ApiConfig(AppConfig):
    name = 'api'
    model = joblib.load("C:/Users/User/Music_Recommendation_App/MusicApp/music_predict.joblib")