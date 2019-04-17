from django.db import models

class New_Result_Manager(models.Manager):
    def search_bar(self,keyword):
        if self.filter(Person_Name__icontains=keyword):
            print('\nMatching Results are :- \n')
            for x in self.filter(Person_Name__icontains=keyword):
                print(x)
        else:   
            print('No Match Found!')
    

class Result(models.Model):
    Person_Name = models.CharField(max_length=15)
    Pull_Ups = models.IntegerField()
    Push_Ups = models.IntegerField()

    def __str__(self):
        return str(self.Person_Name) + '- Results'


class Modify_Result(models.Model):
    Person_Name = models.CharField(max_length=15)
    Pull_Ups = models.IntegerField()
    Push_Ups = models.IntegerField()
    Chin_Ups = models.IntegerField()
    
# the magic lines of the movie
    objects = New_Result_Manager()

    def __str__(self):
        return str(self.Person_Name) + '-> Modify-Results'


    
