from django.contrib import admin
from django.urls import path , include
from rest_framework import routers


router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RecApp.urls')),
    path('RecApp/',include('django.contrib.auth.urls')),
    #path('api/', include(router.urls)),
]
