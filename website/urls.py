from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_page),

    # just including the path
    path('first_app/',include('first_app.urls')),

    # for testing app
    path('test/' , include('test_app.urls')),

    # my first website like project
    path('mili/',include('mili.urls') ),

]











