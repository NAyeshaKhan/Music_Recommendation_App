from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Playlist


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

class PlaylistCreateForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ('title',)
        labels = {'title':'Playlist Name'}
    
    def __init__(self, *args, **kwargs):
        super(PlaylistCreateForm,self).__init__(*args, **kwargs)
        self.fields['title'].required= False
        self.fields