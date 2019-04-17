from django.db import models

# here my manager for registration come in action
'''
class Any_Model_Manager(models.Manager):
    def search_box(self,keyword):
        for x in self.filter(name__icontains=str(keyword)):
            print(x)

class Any_Model_Manager2(models.Manager):
    def search_acc_gender(self,gender_please):
         for x in self.filter(gender=gender_please.lower()):
            print(x)
'''
# and it's ends here like manager deaths

class Divide_into_gender(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='male')

# for page2
class Registration(models.Model):

    choice_field = [
                ('male' , 'Male'),
                ('female' , 'Female'),
            ]

    age_choice = [
            (18,'18'), (19,'19'),
            (20,'20'), (21,'21'),
            (22,'22'), (23,'23'),(24,'24')
            ]

    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(choices=age_choice)
    gender = models.CharField(max_length=6,choices=choice_field)
    roll = models.CharField(max_length=6)
    email = models.EmailField()
    percent = models.PositiveIntegerField()

    objects = models.Manager()
    objects_two = Divide_into_gender()
    
    # game changing line
    #objects = Any_Model_Manager()

    # our second model manager
    #objects2 = Any_Model_Manager2()

    def __str__(self):
        name_split = self.name.split(' ')
        return str(name_split[0] + '-' +str(self.roll))

# for page3
class Examination(models.Model):
    
    roll = models.CharField(max_length=6)
    weight = models.PositiveIntegerField()
    chest = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    pull_ups = models.PositiveIntegerField()
    time = models.PositiveIntegerField()
    marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.roll)+' '+str('Examination')






