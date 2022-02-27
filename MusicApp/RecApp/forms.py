from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ("username", "age", "gender", "email", "password1", "password2")

