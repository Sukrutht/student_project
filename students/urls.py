from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),

]
