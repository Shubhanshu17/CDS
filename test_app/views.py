from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from . import forms
from . import models

# Create your views here.
def radio_form_method(request):
    f = forms.Radio_Form()
    return render(request,'radio.html',{'f' : f})
    

def radio_form_method2(request):
    f2 = forms.Radio_Form(request.POST)
    radio_value2='Nothing'
    radio_value='Nothing'
    if f2.is_valid():
        radio_value = f2.cleaned_data.get('radio')
        radio_value2 = f2.cleaned_data.get('select')
    return render(request,'radio.html',{'f2' : f2,'radio_value' : radio_value,'radio_value2' : radio_value2})


def template_view_method(request):
    return render(request,'template_view.html')

class Template_view_class(TemplateView):
    template_name = 'template_view.html'

# after this we just make sure with the list and detail view 

class InformationsListView(ListView):
    model = models.Informations
    template_name = 'informations.html'
    queryset = models.Informations.objects.filter(first_name__startswith='S')

class InformationsDetailView(DetailView):
    model = models.Informations
    template_name = 'details.html'




