from django.shortcuts import render
from dashboards import jwt_generator
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name=None)
def show_emp_dashboards(request):
    return render(request, 'dashboards/emp_dashboard.html')

@login_required(redirect_field_name=None)
def show_project_dashboards(request):
    return render(request, 'dashboards/project_dashboard.html')