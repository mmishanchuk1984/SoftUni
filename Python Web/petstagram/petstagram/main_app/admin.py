from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile, Pet, PetsPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetsPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
