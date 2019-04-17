from django  import forms

class Radio_Form(forms.Form):
    radio_choices = [ 
            ('male','Mr. Male'),
            ('female' , 'Miss. Female')
            ]

# for radio button in django forms
# input way is same 
    radio = forms.CharField(label='Your Gender ',widget=forms.RadioSelect(choices=radio_choices))

# drop down menu in django forms
# input way is same
    select = forms.ChoiceField(label='Please choose any one ',choices=radio_choices)

# check box in django forms
    demo = forms.CharField(label='Please choose multiple',widget = forms.CheckboxSelectMultiple(choices=radio_choices))


