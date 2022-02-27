from django.urls import path
from RecApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard')
]
