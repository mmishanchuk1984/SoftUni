# Generated by Django 4.0.1 on 2022-02-04 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_department_alter_employee_company_alter_employee_egn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]
