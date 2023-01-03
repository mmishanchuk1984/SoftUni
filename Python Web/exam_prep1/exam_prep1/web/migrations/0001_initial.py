# Generated by Django 4.0.2 on 2022-02-21 23:02

import django.core.validators
from django.db import migrations, models
import exam_prep1.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep1.web.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep1.web.models.validate_only_letters])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[exam_prep1.web.models.MaxFileSizeInMbValidator(5)])),
            ],
        ),
    ]
