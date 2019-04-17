from django.urls import path
from . import views

urlpatterns = [
        path('registration/',views.registration_method),
        path('valid_registration/',views.valid_registration_method),

        path('examination/', views.examination_method),
        path('valid_examination/',views.valid_examination_method),

        path('check/',views.check_in_database_method),
        path('valid_check/',views.valid_check_in_database_method),
        
]
