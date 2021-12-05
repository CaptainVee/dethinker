from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    faculty=models.CharField(max_length=100)

class Questions(models.Model):
    course_code=models.CharField(max_length=100)
    course_title=models.CharField(max_length=100)
    session=models.DateField()

class Answers(models.Model):
    answer=models.CharField(max_length=100) #for theory. not sure how to do the obj part

class School(models.Model):
    school_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
