# Generated by Django 4.0.1 on 2022-02-04 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0019_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('company', 'first_name')},
        ),
    ]
