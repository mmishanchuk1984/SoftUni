import profile

from django.shortcuts import render, redirect

from petstagram.main_app.forms import EditProfileForm, CreateProfileForm, DeleteProfileForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetsPhoto, Profile, Pet
from petstagram.main_app.views import pets


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid:
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {'form': form}
    return render(request, template_name, context)


def show_profile_details(request):
    profile = get_profile()
    pet_photos = PetsPhoto.objects.filter(tagged_pets__user_profile=profile)
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)
    pets = Pet.objects.all()

    context = {'profile': profile,
               'total_likes_count': total_likes_count,
               'total_pet_photos_count': total_pet_photos_count,
               'pets': pets
               }
    return render(request, 'main/profile_details.html', context)


# def create_profile(request):
#     if request.method == 'POST':
#         # create form with POST
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         # create empty form
#         form = CreateProfileForm()
#
#     context = {'form': form}
#
#     return render(request, 'profile_create.html', context)

#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         # create form with POST
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile page')
#     else:
#         # create empty form
#         form = EditProfileForm(instance=profile)
#
#     context = {'form': form}
#
#     return render(request, 'profile_edit.html', context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'main/profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile page', get_profile(), 'main/profile_edit.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')
