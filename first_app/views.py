from django.shortcuts import render
from .forms import First_Form,Radio_Form
from .models import Modify_Result

def from_url(request,url):
    return render(request,'first_app.html',{'url' : url})

def first_form_method(request):
    return render(request,'first_form.html',{})

def first_form_method2(request):
    name = request.GET['input_name']
    return render(request,'first_form.html',{"name" : name})

# .........................Html forms in Django Way

def first_django_form_method(request):

    f = First_Form(initial={'Person_Name' : 'Shubham...etc','Pull_Ups' : 2, 'Push_Ups' : 10, 'Chin_Ups' : 12} )

    f2 = Radio_Form()

    return render(request,'forms.html',{'f' : f,'f2' : f2})

def first_django_form_method2(request):
    error_time = 0
    good,radio_input = '',''
    f2 = Radio_Form(request.POST)
    if f2.is_valid():
        radio_input = f2.cleaned_data.get('RADIO')

    f = First_Form(request.POST)
    f_database_read  = Modify_Result.objects

    if f.is_valid():
        name = f.cleaned_data.get('Person_Name').capitalize()
        pull = f.cleaned_data.get('Pull_Ups')
        push = f.cleaned_data.get('Push_Ups')
        chin = f.cleaned_data.get('Chin_Ups')
        
        name_,pull_,push_,chin_ = name,pull,push,chin 

        f_database = Modify_Result(Person_Name=name_,Pull_Ups=pull_,Push_Ups=push_,Chin_Ups=chin)

        
        if f_database_read.filter(Person_Name=name).exists():
            error_time = 1
            good = 0
        else:
            f_database.save()
            good = 1
            
    else:
        name_,pull_,push_,chin_= '','','',''


    return render(request,'forms.html',{ 'f':f ,'good' : good ,'error_time' : error_time ,'radio_input': radio_input} )









