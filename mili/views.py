from django.shortcuts import render
from .forms import Registration_Form,Examination_Form,Check_Form
from .models import Registration,Examination
from random import randrange

# it's a forms page in which user enters his data
def registration_method(request):
    # it's a forms page which shows you a form

    default_values = {
            'name' : 'Name Surname',
            'email' : '@gmail.com',
            'percent' : '',
            }

    # it's boring form access like database
    registration_form = Registration_Form(initial=default_values)
    
    # same line repeat again and again
    return render(request,'mili_registration.html',{'registration_form' : registration_form})

def valid_registration_method(request):
    reg_form = Registration_Form(request.POST)

    # define some variable for unboundlocal variable error
    li = []
    roll_,name_,email_,exists_in_database= 0,'','',False

    # taking input from form
    if reg_form.is_bound:
        if reg_form.is_valid():
            name_ = reg_form.cleaned_data.get('name').title()
            age_ = reg_form.cleaned_data.get('age')
            gender_ = reg_form.cleaned_data.get('gender')
            email_ = reg_form.cleaned_data.get('email')
            percent_ = reg_form.cleaned_data.get('percent')

            # generating roll number
            for x in range(6):
                li.append(str(randrange(0,9)))
            roll_ = int(''.join(li))

            # saving it to the database
            registration_database = Registration(name=name_,age=age_,gender=gender_,email=email_,percent=percent_,roll=roll_)

            reg_database_check = Registration.objects
            exists_in_database = reg_database_check.filter(roll=roll_).exists()

            if not exists_in_database:
                registration_database.save()
    
    # this is our repeating line
    return render(request,'mili_registration.html',{'registration_form' : reg_form,'roll_number':roll_,'candidate_name' : name_.split(' ')[0],'email_id':email_ ,'exists_in_database' : exists_in_database})

#.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

def examination_method(request):
    
    # once again this method provide a forms page
    examination_form = Examination_Form()

    return render(request,'mili_examination.html',{'examination_form' : examination_form})

def valid_examination_method(request):
    
    # for accessing database and forms
    exam_form = Examination_Form(request.POST)
    reg_data_check = Registration.objects
    exam_data_check = Examination.objects
    save = False
    name_from_reg = ['None'] 

    if exam_form.is_bound:
        if exam_form.is_valid():
            roll_ = exam_form.cleaned_data.get('roll')
            weight_ = exam_form.cleaned_data.get('weight')
            chest_ = exam_form.cleaned_data.get('chest')
            height_ = exam_form.cleaned_data.get('height')
            pull_ups_ = exam_form.cleaned_data.get('pull_ups')
            time_ = exam_form.cleaned_data.get('time')
            marks_ = exam_form.cleaned_data.get('marks')

            name_ = reg_data_check.get(roll=roll_)

            examination_database = Examination(roll=roll_,weight=weight_,chest=chest_,height=height_,pull_ups=pull_ups_,time=time_,marks=marks_)
            
            if not exam_data_check.filter(roll=roll_).exists():
                examination_database.save()
                if exam_data_check.filter(roll=roll_).exists():
                    save = True
                    name_from_reg[0]=name_.name
            else:
                save='refresh'


    return render(request,'mili_examination.html',{'save' : save,'examination_form' : exam_form,'name':name_from_reg})

# .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

def check_in_database_method(request):

    # once again it's a forms page 
    check_form = Check_Form()
    return render(request,'mili_check.html',{'check_form' : check_form})


def valid_check_in_database_method(request):

    check_form = Check_Form(request.POST)
    reg_database_check = Registration.objects   # database 
    exam_database_check = Examination.objects   # ready for retrieve

    # some essential variable for that
    attendence = 'absent'
    failure = ['pass','pass','pass','pass','pass','pass']
    can_list = []                               # candidate list
    roll_not_found = False
    final_result = 'final_fail'

    if check_form.is_bound:
        if check_form.is_valid():
            roll_check =  check_form.cleaned_data.get('roll')

                # All logic for result.html going to happen here
            
            if reg_database_check.filter(roll=roll_check):
                if exam_database_check.filter(roll=roll_check):
                    attendence = 'present'

                if attendence == 'present':
                    can_id_get = exam_database_check.get(roll=roll_check)
                    can_id_get2 = reg_database_check.get(roll=roll_check)
                    
                    # Candidate Basic Info.
                    can_list.append(can_id_get2.name.split(' '))
                    can_list.append(roll_check)
                    can_list.append(can_id_get2.age)
                    can_list.append(can_id_get2.gender)

                    # Candidate Exam Info.
                    can_list.append(can_id_get.chest)
                    can_list.append(can_id_get.height)
                    can_list.append(can_id_get.pull_ups)
                    can_list.append(can_id_get.time)
                    can_list.append(can_id_get.marks)
                    can_list.append(can_id_get.weight)

                    # algorithm for ''pass'' or failure of the candidate
                    # failure list start with 0(index)
                    if can_list[4] < 77:
                        failure[0] = 'fail'
                    if can_list[5] < 167:
                        failure[1] = 'fail'
                    if can_list[6] < 8:
                        failure[2] = 'fail'
                    if can_list[7] > 360:
                        failure[3] = 'fail'
                    if can_list[8] < 33:
                        failure[4] = 'fail'
                    if can_list[9] < 60:
                        failure[5] = 'fail'

                    if not 'fail' in failure:
                        final_result = 'final_pass'

                    return render(request,'mili_result.html',{'can_list' : can_list,'roll_check' : roll_check,'failure' : failure,'final_result' : final_result})
            else:
                roll_not_found = True

    return render(request,'mili_check.html',{'check_form' : check_form,'roll_not_found' : roll_not_found})

#.........................................








