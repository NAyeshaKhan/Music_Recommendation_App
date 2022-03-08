from django.urls import path
from . import views

app_name = "RecApp"

urlpatterns = [
    path('', views.home, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('playlist/', views.playlist_read, name='playlist_read'),
    path('createplaylist/', views.playlist_create, name='playlist_create'),
    path('delete/<int:id>/', views.playlist_delete,name='playlist_delete')    
]
