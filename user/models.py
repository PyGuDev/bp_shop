from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, last_name=None, first_name=None, patronymic=None,
                    phone_number=None, date_of_birth=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = models.CharField('Номер телефона', max_length=12, blank=True, null=True)
    email = models.CharField('Email', max_length=100, unique=True)
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=200, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=200, blank=True, null=True)
    patronymic = models.CharField('Отчество', max_length=200, blank=True, null=True)
    username = models.CharField('Логин', max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronymic)

    def __str__(self):
        return self.email

