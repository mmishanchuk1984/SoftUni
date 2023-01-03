from django.shortcuts import render, redirect

from petstagram.main_app.models import PetsPhoto
from petstagram.main_app.helpers import get_profile


def show_photo_details(request, pk):
    pet_photo = PetsPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {'pet_photo': pet_photo}
    return render(request, 'main/photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetsPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo details', pk)


def add_pet_photo(request):
    return render(request, 'main/photo_create.html')


def edit_pet_photo(request):
    return render(request, 'main/photo_edit.html')
