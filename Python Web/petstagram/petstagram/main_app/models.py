import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main_app.validators import only_letters_validator, max_mb_size_validator

UserModel = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"

    GENDERS = [(x, x) for x in [MALE, FEMALE, DO_NOT_SHOW]]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH), only_letters_validator,)

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH), only_letters_validator)
    )
    profile_picture = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=max(len(x) for x, _ in GENDERS), null=True, blank=True,
                              default=DO_NOT_SHOW)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    # Constants
    NAME_MAX_LENGTH = 30
    MIN_DATE = datetime.date(1920, 1, 1)

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in [CAT, DOG, FISH, BUNNY, PARROT, OTHER]]
    # Fields(columns in table)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    type = models.CharField(choices=TYPES, max_length=max(len(x) for x, _ in TYPES))
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    # One to One relations

    # One to many relations
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,)
    # Many to Many relations

    # Properties
    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # __ Methods
    def __str__(self):
        return f"{self.name}"

    # Meta
    class Meta:
        unique_together = ('user', 'name')


class PetsPhoto(models.Model):
    photo = models.ImageField(
        validators=(max_mb_size_validator,)
    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
