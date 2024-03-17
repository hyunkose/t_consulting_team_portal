from django.shortcuts import render
from commons.models import EmployeeInfo, ProjectInfo, VacationInfo, EmployeeStatus
from django.contrib.auth.decorators import login_required
from commons import extra_info_generator

import pandas as pd

@login_required(redirect_field_name=None)
def show_emp_info(request):
    if request.method == 'GET':
        emp_obj = EmployeeInfo.objects.all()
        return render(request, 'data_read/read_emp_info.html', context = { 'emp_obj': emp_obj })
    
@login_required(redirect_field_name=None)
def show_status_info(request):
    if request.method == 'GET':
        status_obj = EmployeeStatus.objects.all()
        emp_obj = EmployeeInfo.objects.all()

    extra_info_generator.emp_cd_converter(status_obj, emp_obj)
        
    return render(request, 'data_read/read_status_info.html', context = { 'status_obj': status_obj})

@login_required(redirect_field_name=None)
def show_proj_info(request):
    if request.method == 'GET':
        proj_obj = ProjectInfo.objects.all()
        emp_obj = EmployeeInfo.objects.all()
        
        extra_info_generator.emp_cd_converter(proj_obj, emp_obj)

        return render(request, 'data_read/read_project_info.html', context = { 'proj_obj': proj_obj})

@login_required(redirect_field_name=None)
def show_vacation_info(request):
    if request.method == 'GET':
        vacation_obj = VacationInfo.objects.all()
        emp_obj = EmployeeInfo.objects.all()

        extra_info_generator.emp_cd_converter(vacation_obj, emp_obj)
        
        return render(request, 'data_read/read_vacation_info.html', context = { 'vacation_obj': vacation_obj})