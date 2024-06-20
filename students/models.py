from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from .validators import validate_name, validate_course, validate_college, validate_department

class Student(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    email = models.EmailField(validators=[EmailValidator()])
    course = models.CharField(max_length=100, validators=[validate_course])
    college = models.CharField(max_length=100, validators=[validate_college])

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    email = models.EmailField(validators=[EmailValidator()])
    salary = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    department = models.CharField(max_length=100, validators=[validate_department])

    def __str__(self):
        return self.name

