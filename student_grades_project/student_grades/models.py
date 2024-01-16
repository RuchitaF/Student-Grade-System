from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    module1_grade = models.CharField(max_length=5)
    module2_grade = models.CharField(max_length=5)
    module3_grade = models.CharField(max_length=5)
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    module1_grade = models.CharField(max_length=5)
    module2_grade = models.CharField(max_length=5)
    module3_grade = models.CharField(max_length=5)
