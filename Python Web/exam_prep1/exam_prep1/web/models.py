from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not all(c.isalpha() for c in value):
        raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError('Max file size is 5.00 MB')


# Create your models here.


class Profile(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15
    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(MinLengthValidator(NAME_MIN_LEN), validate_only_letters), )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(MinLengthValidator(NAME_MIN_LEN), validate_only_letters), )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),), )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),), )


class Expense(models.Model):

    title = models.CharField(max_length=30)
    expense_image = models.URLField()
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    class Meta:
        ordering = ('title', 'price')

