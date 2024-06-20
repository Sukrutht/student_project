from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Employee
from django.core.paginator import Paginator
from .forms import StudentForm, EmployeeForm

students = []

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_edit(request, id):  
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'edit': True})

def student_delete(request, id): 
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})


def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_list(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'students/student_list.html', {'page_obj': page_obj})

# ................................................................................................................


def employee_list(request):
    employees = Employee.objects.all()
    for employee in employees:
        print(employee.id)
    return render(request, 'students/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm()
    return render(request, 'students/add_employee.html', {'form': form})


def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'students/employee_edit.html', {'form': form})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'students/employee_confirm_delete.html', {'employee': employee})


def employee_list(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/employee_list.html', {'page_obj': page_obj})


