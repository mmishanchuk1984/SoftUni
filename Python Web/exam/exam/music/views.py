from django.shortcuts import render, redirect

from exam.music.forms import CreateProfileForm, DeleteProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from exam.music.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    albums_count = len(albums)

    context = {'profile': profile, 'albums': albums, 'albums_count': albums_count}

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {'form': form, 'no_profile': True}
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile-delete.html', context)


def show_profile(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)
    context = {'profile': profile, 'albums_count': albums_count, 'albums': albums}
    return render(request, 'profile-details.html', context)


def create_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {'form': form}
    return render(request, 'add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'delete-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {'album': album}
    return render(request, 'album-details.html', context)
