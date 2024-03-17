from django.db import models

class CSMDatasource(models.Model):
    csm_key = models.AutoField(primary_key=True) 
    std_dt = models.CharField(max_length=100)
    close_part = models.CharField(max_length=100)
    company_cd = models.CharField(max_length=100)
    company_nm = models.CharField(max_length=100)
    contents = models.CharField(max_length=100)
    contract_start_date = models.CharField(max_length=100)
    contract_end_date = models.CharField(max_length=100)
    user_nm = models.CharField(max_length=100)
    close_time = models.IntegerField()
    total_contract_time = models.IntegerField()

    class Meta:
        db_table = 'csm_data_source'

class Masterdate(models.Model):
    std_dt = models.CharField(primary_key=True, max_length=100)
    
    class Meta:
        db_table = 'master_date'

class EmployeeInfo(models.Model):
    emp_info_key = models.AutoField(primary_key=True) 
    std_dt = models.CharField(max_length=100)
    emp_cd = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emp_level = models.CharField(max_length=100)
    hired_date = models.CharField(max_length=100)
    total_vacations = models.FloatField()
    
    class Meta:
        db_table = 'employee_info'

class EmployeeStatus(models.Model):
    emp_status_key = models.AutoField(primary_key=True)
    std_dt = models.CharField(max_length=100)
    emp_cd = models.IntegerField()
    status = models.CharField(max_length=100)
    leave_date = models.CharField(max_length=100)
    rest_start_date = models.CharField(max_length=100)
    rest_end_date = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'employee_status'

class ProjectInfo(models.Model):
    project_key = models.AutoField(primary_key=True)
    emp_cd = models.IntegerField()
    client = models.CharField(max_length=100)
    project_start_date = models.CharField(max_length=100)
    project_end_date = models.CharField(max_length=100)
    client_location = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)

    class Meta:
        db_table = 'project_info'

class VacationInfo(models.Model):
    vacation_key = models.AutoField(primary_key=True)
    emp_cd = models.IntegerField()
    vacation_start_date = models.CharField(max_length=100)
    vacation_end_date = models.CharField(max_length=100)
    vacation_type = models.CharField(max_length=100)
    vacation_days= models.IntegerField()

    class Meta:
        db_table = 'vacation_info'
