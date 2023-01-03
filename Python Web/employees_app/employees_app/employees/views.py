import random

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

# def home(request):
#     html = f'<h1>{request.method}: This is home!</h1>'
#     return HttpResponse(html, content_type= 'application/xml')
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def home(request):
    print(reverse_lazy('home page'))
    print(reverse_lazy('departments list'))
    print(reverse_lazy('department details', kwargs={'id': 7,}))
    num = random.randint(0, 10)
    context = {'number': num}

    return render(request, 'index.html', context)


def department_details(request, id):
    return HttpResponse(f'This is a department {id}')


def not_found(request):
    return HttpResponseNotFound()


def list_of_departments(request):
    context = {
        'department': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all()
    }
    return render(request, 'list_departments.html', context)


def redirect_to_home(request):
    # return HttpResponseRedirect(redirect_to='/')
    return redirect('home page')

