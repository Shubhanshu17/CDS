from django.urls import path
from . import views

urlpatterns = [

        path('radio/', views.radio_form_method),
        path('radio_value/', views.radio_form_method2),

        path('views1/',views.template_view_method),
        path('views2/',views.Template_view_class.as_view()),

        path('list/' , views.InformationsListView.as_view()),
        path('detail/<int:pk>' , views.InformationsDetailView.as_view()),

        ]
