from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Create your forms here.

class CustomUserCreationForm(UserCreationForm):
    #class Meta:
        #model=CustomUser
        #fields = "__all__"
    class Meta(UserCreationForm.Meta):
        #keeps additional information about the form and extends UserCreationForm
        fields = UserCreationForm.Meta.fields + ("email",)        
      
      