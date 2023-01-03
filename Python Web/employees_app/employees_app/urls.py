from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, not_found, redirect_to_home

# Mandatory tuple or list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),  # localhost:8000 -> home
    path('gotohome/', redirect_to_home, name='home page'),

    path('departments/', include('employees_app.employees.urls')),
    path('templates', include('employees_app.template_examples.urls'))
]
