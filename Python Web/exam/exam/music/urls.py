from django.urls import path

from exam.music.views import create_profile, show_profile, delete_profile, create_album, show_index, edit_album, \
    delete_album, album_details

urlpatterns = (
    path('', show_index, name='show index'),

    path('album/add/', create_album, name='create album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('album/details/<int:pk>', album_details, name ='album details'),


    path('profile/detaels', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='profile delete'),
)
