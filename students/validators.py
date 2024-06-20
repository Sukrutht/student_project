from django.core.exceptions import ValidationError

def validate_name(value):
    if not value.replace(' ', '').isalpha():  
        raise ValidationError('Name should only contain letters.')

def validate_course(value):
    if not value.replace(' ','').isalpha():
        raise ValidationError('Course name should only contain alphabets.')

def validate_college(value):
    if not value.replace(' ','').isalpha():
        raise ValidationError('College name only contain letters.')

def validate_department(value):
    if not value.replace(' ','').isalpha():
        raise ValidationError('Department name should only contain letters.')   


