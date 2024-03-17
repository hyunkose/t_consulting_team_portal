from django.contrib import admin
from django.urls import path
from data_create import views as create_view
from data_read import views as read_view
from data_delete import views as delete_view
from dashboards import views as dashboards_view
from commons import views as commons_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboards_view.show_emp_dashboards, name="dashboards_emp"),
    path('accounts/login/', commons_view.show_login, name="login"),
    path('accounts/logout/', commons_view.logout_view, name="logout"),
    
    path('dashboards_emp/', dashboards_view.show_emp_dashboards, name="dashboards_emp"),
    path('dashboards_project/', dashboards_view.show_project_dashboards, name="dashboards_project"),
    
    path('create_empinfo/', create_view.empinfo_create_form, name="create_empinfo"),
    path('create_status/', create_view.statusinfo_create_form, name="create_statusinfo"),
    path('create_project/', create_view.projectinfo_create_form, name="create_projectinfo"),
    path('create_vacation/', create_view.vacationinfo_create_form, name="create_vacationinfo"),
    
    path('read_emp/', read_view.show_emp_info, name="read_empinfo"),
    path('read_status/', read_view.show_status_info, name="read_statusinfo"),
    path('read_proj/', read_view.show_proj_info, name="read_projectinfo"),
    path('read_vacation/', read_view.show_vacation_info, name="read_vacation_info"),
        
    path('delete_emp/', delete_view.emp_delete_form, name="delete_emp"),
    path('delete_status/', delete_view.status_delete_form, name="delete_status"),
    path('delete_project/', delete_view.project_delete_form, name="delete_project"),
    path('delete_vacation/', delete_view.vacation_delete_form, name="delete_vacation"),
]
