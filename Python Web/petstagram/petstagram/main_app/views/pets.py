from django.views import generic as views
from petstagram.main_app.forms import CreatePetForm, EditPetForm, DeletePetForm


class CreatePetView(views.CreateView):
    form_class = CreatePetForm
    template_name = 'main/pet_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    form_class = EditPetForm
    template_name = 'main/pet_edit.html'


class DeletePetView(views.DeleteView):
    form_class = DeletePetForm
    template_name = 'main/pet_delete.html'

