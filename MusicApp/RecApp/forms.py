from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Create your forms here.

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
    #class Meta(UserCreationForm.Meta):
        model=CustomUser
        #keeps additional information about the form and extends UserCreationForm
        #fields = UserCreationForm.Meta.fields + ("email","age","gender",)
        fields = ("username", "email", "age", "gender", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user        
      
      