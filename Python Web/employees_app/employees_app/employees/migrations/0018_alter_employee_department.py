# Generated by Django 4.0.1 on 2022-02-04 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
            preserve_default=False,
        ),
    ]
