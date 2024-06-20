from django import forms
from .models import Student, Employee

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'course', 'college']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','salary','department']




