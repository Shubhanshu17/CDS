from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# for testing the list and detail views of Django

class Informations(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    # we call the list view from the age
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name





