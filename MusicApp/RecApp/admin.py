from django.contrib import admin
from .models import CustomUser, Playlist, Song
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    
    fieldsets= (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'age',
                    'gender',
                )
            }
        
        )
    
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Playlist)
admin.site.register(Song)



