from django.views import  generic as views
from django.shortcuts import render

from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetsPhoto


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = PetsPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'
