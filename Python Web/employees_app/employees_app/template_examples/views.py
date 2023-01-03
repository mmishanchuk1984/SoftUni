from django.shortcuts import render


# Create your views here.
from employees_app.employees.models import Employee, Department


def index(request):

    context = {
        'n1': 123,
        'n2': 321,
        'n3': 200,
        'title': 'Employees list!',
        'employees': Employee.objects.order_by('-department').all(),
        'departments_list': [d.dep_name for d in Department.objects.all()]
    }
    return render(request, 'templates_examples/index.html', context)
