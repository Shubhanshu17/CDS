from django import forms
from .models import Registration
from .models import Examination

class Registration_Form(forms.ModelForm):
    
    class Meta:
        model = Registration
        exclude = ['roll',]
        labels = {
                'name' : 'Candidate Name ',
                'age' : 'Age ',
                'gender' : 'Gender ',
                'email' : 'Email ID ',
                'percent' : 'Class 10(in %)',
                }

    def clean_percent(self):
        percentage = self.cleaned_data.get('percent')
        if percentage < 40:
            raise forms.ValidationError('You must have atleast 40%')

        return percentage

    def clean_email(self):
        email_id = self.cleaned_data.get('email')
        if not email_id.endswith('@gmail.com'):
            raise forms.ValidationError('You must signed in as Gmail')

        return email_id

    def clean_age(self):
        age_check = self.cleaned_data.get('age')
        if age_check < 18 or age_check > 24:
            raise forms.ValidationError('Age must lies b/w 18-24 below')

        return age_check

    def clean_name(self):
        name_check = self.cleaned_data.get('name')
        if name_check == 'Name Surname':
            raise forms.ValidationError('You can\'t use Default Name')

        return name_check

#......................................

class Examination_Form(forms.ModelForm):

    class Meta:
        model = Examination
        fields = '__all__'
        labels = {
                'roll' : 'Roll Number ',
                'weight' : 'Weight(in Kg) ',
                'chest' : 'Chest(in Cm) ',
                'height' : 'Height(in Cm) ',
                'pull_ups' : 'Pull Ups ',
                'time' : 'Running Time(in sec) ',
                'marks' : 'Test Marks'
                }

    # for checking the existance of candidate

    def clean_roll(self):
        roll_num = self.cleaned_data.get('roll')
        reg_database = Registration.objects

        if not reg_database.filter(roll=roll_num).exists():
            raise forms.ValidationError("Roll Number Doesn't Matches!")

        return roll_num

    #......................................

class Check_Form(forms.Form):

    roll = forms.CharField(label='Roll Number',initial="",widget=forms.PasswordInput)

    def clean_roll(self):
        roll_num = self.cleaned_data.get('roll')
        roll_exists = Registration.objects

        if not roll_num.isdigit():
            raise forms.ValidationError('Please Enter a Valid Number')
        if not roll_exists.filter(roll=roll_num).exists():
            raise forms.ValidationError('Roll Number Doesn\'t Exists')

        return roll_num

















