from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True, help_text='Email')
    age = forms.IntegerField(required=True,help_text='Age')
    gender = forms.CharField(max_length=20, required=True, help_text='Gender')

    class Meta:
        model = User
        fields = ("username", "age", "gender", "email", "password1", "password2")

