from django import forms
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль')
    date_of_birth = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name',
                  'patronymic', 'phone_number', 'date_of_birth', 'password']
