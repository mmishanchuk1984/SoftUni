# Generated by Django 4.0.1 on 2022-02-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
