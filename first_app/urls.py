from django.urls import path
from . import views

urlpatterns = [
    path('from_url/<url>/',views.from_url),
    path('form/',views.first_form_method),
    path('form2/',views.first_form_method2),
# here's comes the django way for forms
    path('django_form/',views.first_django_form_method),
    path('django_form2/',views.first_django_form_method2),


]
