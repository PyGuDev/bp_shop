from django.forms import ModelForm
from .models import CustomUser


class UserCreationForm(ModelForm):
    class Meta:
        model = CustomUser