from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from commons.models import EmployeeInfo, EmployeeStatus, ProjectInfo, VacationInfo
from commons import extra_info_generator

import json
from datetime import datetime

@csrf_exempt
def empinfo_create_form(request):
    if request.method == 'GET':
        return render(request, 'data_create/create_emp_info.html')
    elif request.method == 'POST':
        data = json.loads(request.body)

        std_dt = data['emp_hired_date']

        emp_key_obj = EmployeeInfo.objects.latest('emp_info_key')
        emp_cd_obj = EmployeeInfo.objects.latest('emp_cd')

        emp_info_key = emp_key_obj.emp_info_key+1
        emp_cd = emp_cd_obj.emp_cd+1
        emp_name = data['emp_name']
        email = data['emp_email']
        emp_level = data['emp_level']
        hired_date = data['emp_hired_date']
        total_vacations = data['total_vacations']
        
        emp_info_obj = EmployeeInfo(
            emp_info_key = emp_info_key,
            std_dt = std_dt,
            emp_cd = emp_cd,
            emp_name = emp_name,
            email = email,
            emp_level = emp_level,
            hired_date = hired_date,
            total_vacations = total_vacations
        )

        emp_info_obj.save()

        return JsonResponse({ 'message': 'emp data save success'}, safe=False)
    
@csrf_exempt
def statusinfo_create_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_create/create_status_info.html', context = {'emp_obj': emp_obj})
    elif request.method == 'POST':
        data = json.loads(request.body)

        std_dt = ''
        email = data['emp_email'],
        status = data['emp_status'],
        rest_start_date = data['rest_start_date'],
        rest_end_date = data['rest_end_date'],
        leave_date = data['leave_date']

        status_key_obj = EmployeeStatus.objects.latest('emp_status_key')
        emp_info_obj = EmployeeInfo.objects.get(email = email[0])
        emp_cd = emp_info_obj.emp_cd

        if status[0] == '휴직':
            std_dt =  rest_start_date
        elif status[0] == '퇴사':
            std_dt =  leave_date
    
        emp_status_insert_obj = EmployeeStatus(
            emp_status_key = status_key_obj.emp_status_key+1,
            std_dt = std_dt,
            emp_cd = emp_cd,
            status = status[0],
            leave_date = leave_date,
            rest_start_date = rest_start_date[0],
            rest_end_date = rest_end_date[0]
        )

        emp_status_insert_obj.save()

        return JsonResponse({ 'message': 'emp data save success'}, safe=False)

@csrf_exempt
def projectinfo_create_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_create/create_project_info.html', context = {'emp_obj': emp_obj})
    
    elif request.method == 'POST':
        data = json.loads(request.body)

        project_key_obj = ProjectInfo.objects.latest('project_key')

        email = data['emp_email']
        emp_info_obj = EmployeeInfo.objects.get(email = email)
        emp_cd = emp_info_obj.emp_cd


        client = data['client_name']
        client_location = data['client_location']
        project_start_date = data['proj_start_date']
        project_end_date = data['proj_end_date']
        jobs = data['jobs']
        
        proj_info_obj = ProjectInfo(
            project_key = project_key_obj.project_key+1,
            emp_cd = emp_cd,
            client = client,
            client_location = client_location,
            project_start_date = project_start_date,
            project_end_date = project_end_date,
            jobs = jobs
        )

        proj_info_obj.save()

        return JsonResponse({ 'message': 'project data save success'}, safe=False)

@csrf_exempt
def vacationinfo_create_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_create/create_vacation_info.html', context = {'emp_obj': emp_obj})
    
    elif request.method == 'POST':
        data = json.loads(request.body)

        vacation_key_obj = VacationInfo.objects.latest('vacation_key')

        email = data['emp_email']
        emp_info_obj = EmployeeInfo.objects.get(email = email)
        emp_cd = emp_info_obj.emp_cd

        vacation_start_date = data['vacation_start_date']
        vacation_end_date = data['vacation_end_date']
        vacation_type = data['vacation_type']
        vacation_days = data['this_vacation_amt']

        vacation_info_obj = VacationInfo(
            vacation_key = vacation_key_obj.vacation_key+1,
            emp_cd = emp_cd,
            vacation_start_date = vacation_start_date,
            vacation_end_date = vacation_end_date,
            vacation_type = vacation_type,
            vacation_days = vacation_days
        )

        vacation_info_obj.save()

        return JsonResponse({ 'message': 'vacation data save success'}, safe=False)
