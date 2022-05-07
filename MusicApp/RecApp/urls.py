from django.contrib import admin
from django.urls import path,include
from django import urls
from . import views
from rest_framework import routers
from .views import SearchResultsView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
#from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView, PasswordResetDoneView


app_name = "RecApp"
router = routers.DefaultRouter()
router.register('RecApp',views.CustomUserView)
urlpatterns = [
    path('', views.home, name="home"),
    path("songplayer/", views.songplayer, name="songplayer"),
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

    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(template_name='RecApp/password_change.html'),
    ),
    path(
        'RecApp/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='RecApp/password_change_done.html'),
    ),
    path('rating/', views.add_rating, name="rating" ),
    path('song_details/<int:sid>/', views.song_details, name='song_details'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
