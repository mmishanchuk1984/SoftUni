from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.main_app.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from petstagram.main_app.models import Profile, PetsPhoto, Pet
from petstagram.main_app.validators import MaxDateValidator


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'profile_picture': forms.TextInput(attrs={'placeholder': 'Enter URL'}),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'profile_picture': forms.TextInput(attrs={'placeholder': 'Enter URL'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter email'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'min': '1920-01-01'})
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetsPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'profile_picture', 'date_of_birth', 'description', 'gender', 'email')
        # same as fields = ()


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()

        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'}),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
        return self.cleaned_data['date_of_birth']

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
