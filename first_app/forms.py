from django import forms
from .models import Modify_Result


class First_Form(forms.ModelForm):
    class Meta:
        model = Modify_Result
        fields = '__all__'
        label = {'Person_Name' : 'Name ' , 'Pull_Ups' : 'Pull Ups' , 'Push_Ups' : 'Push Ups','Chin_Ups' : 'Chin Ups'}

# required widgets label initial
    '''
    def clean_Person_Name(self):
        return self.Person_Name
    '''    

    def clean_Pull_Ups(self):
        number_pull = self.cleaned_data.get('Pull_Ups')
        if number_pull > 20:
            raise forms.ValidationError('Must Perform Under 20')
        return number_pull
    
    def clean_Push_Ups(self):
        number_push = self.cleaned_data.get('Push_Ups')
        if number_push > 50:
            raise forms.ValidationError('Must Perform Under 50')
        return number_push
    
    def clean_Chin_Ups(self):
        number_chin = self.cleaned_data.get('Chin_Ups')
        if number_chin > 20:
            raise forms.ValidationError('Must Perform Under 20')
        return number_chin


class Radio_Form(forms.Form):
    RADIO = [('male','Male'),
            ('female','Female')]
    gender = forms.CharField(label='Select your gender',widget=forms.RadioSelect(choices=RADIO))

   







