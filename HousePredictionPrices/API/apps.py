import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'API'
    MODEL_FILE = os.path.join(settings.MODELS, "House_Price_Model.joblib")
    model = joblib.load(MODEL_FILE)