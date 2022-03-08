from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Create your forms here.

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
    #class Meta(UserCreationForm.Meta):
        model=CustomUser
        #keeps additional information about the form and extends UserCreationForm
        fields = ("username", "email", "age", "gender", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user              
        
class PredictionForm(forms.ModelForm):
    class Meta:
              model = CustomUser
              fields = ("age", "gender")

    age = forms.IntegerField()
    gender = forms.TypedChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    mood = forms.TypedChoiceField(choices=[(1,'Happy'), (2,'Gloomy'), (3,'Stressed'), (4,'Relaxing'), (5,'Energetic')])