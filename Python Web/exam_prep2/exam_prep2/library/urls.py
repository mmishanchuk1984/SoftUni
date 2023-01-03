from django.urls import path

from exam_prep2.library.views import add_book, show_index, edit_book, book_details, show_profile, create_profile, \
    profile_edit, delete_profile, delete_book

urlpatterns = [
    path('', show_index, name='show index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>', delete_book, name='delete book'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', delete_profile, name='profile delete'),
]
