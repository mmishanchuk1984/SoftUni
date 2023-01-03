from django.urls import path

from employees_app.employees.views import list_of_departments, department_details, not_found

urlpatterns = [
    path('', list_of_departments, name='departments list'),  # localhost:8000/department -> departments
    path('<int:id>', department_details, name='department details'),  # localhost:8000/department/1/ -> department1
    path('not_found/', not_found)
]
