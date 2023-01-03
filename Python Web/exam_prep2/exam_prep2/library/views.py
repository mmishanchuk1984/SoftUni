from django.shortcuts import render, redirect


# Create your views here.
from exam_prep2.library.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm, EditBookForm
from exam_prep2.library.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_base(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'base.html', context)


def show_index(request):
    profile = get_profile()
    books = Book.objects.all()
    books_count = len(books)

    context = {'books': books, 'books_count': books_count, 'profile': profile}

    if not profile:
        return redirect('create profile')
    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {'form': form,}
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit-profile.html', context)


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
    return render(request, 'delete-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateBookForm()

    context = {'form': form}
    return render(request, 'add-book.html', context)


def edit_book(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditBookForm(instance=book)

    context = {'form': form, 'book': book}
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('/')

