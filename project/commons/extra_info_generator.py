from commons.models import EmployeeInfo, ProjectInfo

def emp_cd_converter(target_obj, emp_obj):
    emp_list = [(obj.emp_cd, obj.emp_name) for obj in emp_obj]

    for po in target_obj:
        for code, name in emp_list:
            emp_cd = po.emp_cd
            if emp_cd == code:
                po.emp_cd = name

def get_dropdown_options(option = 'emp_only'):
    distinct_emp_obj = EmployeeInfo.objects.distinct().values_list('email', 'emp_name').order_by('email')
    distinct_proj_obj = ProjectInfo.objects.distinct().values_list('client').order_by('client')
    
    email_list = [obj[0] for obj in distinct_emp_obj]
    name_list = [obj[1] for obj in distinct_emp_obj]
    client_list = [obj[0] for obj in distinct_proj_obj]

    emp_obj = zip(email_list, name_list)

    if option == 'emp_only':
        return emp_obj
    elif option == 'all':
        return emp_obj, client_list