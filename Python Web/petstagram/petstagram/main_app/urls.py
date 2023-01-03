from django.urls import path

from petstagram.main_app.views.generic import HomeView, DashboardView
from petstagram.main_app.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main_app.views.photos import show_photo_details, like_pet_photo, add_pet_photo, edit_pet_photo
from petstagram.main_app.views.profile import show_profile_details, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile/', show_profile_details, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/photo<int:pk>/', show_photo_details, name='photo details'),
    path('photo/like<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', add_pet_photo, name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
)
