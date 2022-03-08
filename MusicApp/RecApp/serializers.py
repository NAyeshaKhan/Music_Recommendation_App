from rest_framework import serializers
from .models import CustomUser 

class CustomUserSerializers(serializers.ModelSerializer): 
    class meta: 
        model=CustomUser 
        fields='__all__'