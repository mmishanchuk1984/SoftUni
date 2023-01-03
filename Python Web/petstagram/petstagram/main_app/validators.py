from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            # invalid case
            raise ValidationError("Value must contain only letters!")


def max_mb_size_validator(max_size):
    def validate(value):
        file_size = value.file.size
        maga_byte_limit = max_size
        if file_size > maga_byte_limit * 1024 * 1024:
            raise ValidationError("Max limit is %sMB" % str(max_size))

    return validate


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must bee greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if value > self.max_date:
            raise ValidationError(f'Date must be smaller than {self.max_date}')
