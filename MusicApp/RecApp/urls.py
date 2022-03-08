from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

app_name = "RecApp"
router = routers.DefaultRouter()
urlpatterns = [
    path('', views.home, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('playlist/', views.playlist_read, name='playlist_read'),
    path('add_playlist/', views.playlist_create, name='playlist_create'),
    path('delete/<int:id>/', views.playlist_delete,name='playlist_delete'),
    path('api/', include(router.urls)),
    path('form/', views.FormView, name='form'),  
    path('search/', SearchResultsView.as_view(), name='search')
    
]
