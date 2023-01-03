from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_username(value):
    if not all(c.isalnum() for c in value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


# Create your models here.
class Profile(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15
    MIN_AGE = 0

    username = models.CharField(max_length=NAME_MAX_LEN,
                                validators=(MinLengthValidator(NAME_MIN_LEN), validate_username), )

    email = models.EmailField()

    age = models.IntegerField(blank=True, null=True, validators=(MinValueValidator(0),))


class Album(models.Model):
    POP = 'Pop Music'
    JAZZ = 'Jazz Music'
    RB = 'R&B Music'
    ROCK = 'Rock Music'
    COUNTRY = 'Country Music'
    DANCE = 'Dance Music'
    HP = 'Hip Hop Music'
    OTHER = 'Other'

    CHOICES = (
        (POP, POP),
        (JAZZ, JAZZ),
        (RB, RB),
        (ROCK, ROCK),
        (COUNTRY, COUNTRY),
        (DANCE, DANCE),
        (HP, HP),
        (OTHER, OTHER),
    )

    album_name = models.CharField(max_length=30)

    artist = models.CharField(max_length=30)

    genre = models.CharField(choices=CHOICES, max_length=30)

    description = models.TextField(null=True, blank=True)

    image_url = models.URLField()

    price = models.FloatField(validators=(MinValueValidator(0),))





