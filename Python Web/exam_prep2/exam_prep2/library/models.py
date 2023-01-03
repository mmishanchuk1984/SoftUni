from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def validate_only_letters(value):
    if not all(c.isalpha() for c in value):
        raise ValidationError('Ensure this value contains only letters.')


class Profile(models.Model):

    first_name = models.CharField(max_length=30, validators=(validate_only_letters,),)

    last_name = models.CharField(max_length=30, validators=(validate_only_letters,),)

    image_url = models.URLField()


class Book(models.Model):

    title = models.CharField(max_length=30)

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)
