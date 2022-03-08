import os
import pandas as pd
from joblib import load
from django.apps import AppConfig
from django.conf import settings

class RecAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RecApp'
