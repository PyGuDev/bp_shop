from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import UserCreationForm
from .models import CustomUser


class SingUpView(CreateView):
    model = CreateView
    form_class = UserCreationForm
    template_name = 'base/auth_modals.html'

    def form_invalid(self, form):
        print(form.errors)
        return redirect('/')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')