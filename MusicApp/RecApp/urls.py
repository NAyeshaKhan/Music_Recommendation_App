from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import SearchResultsView

app_name = "RecApp"
router = routers.DefaultRouter()
router.register('RecApp',views.CustomUserView)
urlpatterns = [
    path('', views.home, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('playlist/', views.playlist_read, name='playlist_read'),
    path('add_playlist/', views.playlist_create, name='playlist_create'),
    path('delete/<int:id>/', views.playlist_delete,name='playlist_delete'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.predict_api, name="predict"),
    path('add_song/<int:id>/', views.add_song, name='addsongtoplaylist'),
    path('playlist_view/<int:id>/', views.playlist_view, name="playlistview"),
    path('song_delete_playlist/<int:sid>/', views.song_delete_playlist, name="song_delete_playlist"),
    path('update/<int:id>', views.update_view ),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="RecApp/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

]
