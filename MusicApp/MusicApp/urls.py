from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RecApp.urls')),
    path('RecApp/',include('django.contrib.auth.urls'))

]
