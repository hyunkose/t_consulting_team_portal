from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from commons.models import EmployeeInfo, EmployeeStatus, ProjectInfo, VacationInfo
from commons import extra_info_generator
import json

@csrf_exempt
def emp_delete_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_delete/delete_emp.html', context = {'emp_obj': emp_obj})
    elif request.method == 'DELETE':
        data = json.loads(request.body)

        message_obj = { 'message': '삭제가 완료되었습니다'}
        try:
            emp_obj = EmployeeInfo.objects.get(email = data['emp_email'], std_dt = data['data_input_date'])
            emp_obj.delete()
        except EmployeeInfo.DoesNotExist:
            message_obj = { 'message': '일치하는 사원 데이터가 없습니다. 데이터 입력일자를 확인해주세요'}
            return JsonResponse(message_obj)

        return JsonResponse(message_obj)

@csrf_exempt
def status_delete_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_delete/delete_status.html', context = {'emp_obj': emp_obj })
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        message_obj = { 'message': '삭제가 완료되었습니다'}

        try:
            emp_obj = EmployeeInfo.objects.get(email = data['emp_email'])
        
            status_obj = EmployeeStatus.objects.get(emp_cd = emp_obj.emp_cd, std_dt = data['vacation_start_date'])
            status_obj.delete()
        except EmployeeStatus.DoesNotExist:
            message_obj = { 'message': '해당 사원의 재직 정보가 없습니다. 데이터 입력일자를 확인해주세요'}
            return JsonResponse(message_obj)

        return JsonResponse(message_obj, safe=False)

@csrf_exempt
def project_delete_form(request):
    if request.method == 'GET':
        emp_obj, client_list = extra_info_generator.get_dropdown_options(option = 'all')
        return render(request, 'data_delete/delete_project.html', context = {'emp_obj': emp_obj, 'client_list':client_list })
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        message_obj = { 'message': '삭제가 완료되었습니다'}

        try:
            emp_obj = EmployeeInfo.objects.get(email = data['emp_email'])
        
            proj_obj = ProjectInfo.objects.get(emp_cd = emp_obj.emp_cd, client = data['client_name'], project_start_date = data['project_start_date'])
            proj_obj.delete()
        except ProjectInfo.DoesNotExist:
            message_obj = { 'message': '해당 사원의 프로젝트 정보가 없습니다. 고객사명 또는 프로젝트 시작일을 확인해주세요'}
            return JsonResponse(message_obj)

        return JsonResponse(message_obj, safe=False)

@csrf_exempt
def vacation_delete_form(request):
    if request.method == 'GET':
        emp_obj = extra_info_generator.get_dropdown_options()
        return render(request, 'data_delete/delete_vacation.html', context = { 'emp_obj': emp_obj })
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        message_obj = { 'message': '삭제가 완료되었습니다'}

        try:
            emp_obj = EmployeeInfo.objects.get(email = data['emp_email'])

            vacation_obj = VacationInfo.objects.get(emp_cd = emp_obj.emp_cd, vacation_start_date = data['vacation_start_date'])
            vacation_obj.delete()
        except VacationInfo.DoesNotExist:
            message_obj = {'message': '해당 사원에 해당하는 휴가 데이터가 없습니다. 휴가 시작일을 확인해주세요'}
            return JsonResponse(message_obj, safe=False)
        
        return JsonResponse(message_obj, safe=False)