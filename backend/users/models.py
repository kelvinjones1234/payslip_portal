from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from departments.models import Department

class UserManager(BaseUserManager):
    def create_user(self, title, email, full_name, ippis_number, gender, phone=None, level=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            title=title,
            email=email,
            full_name=full_name,
            ippis_number=ippis_number,
            # department=department,
            gender=gender,
            phone=phone,
            level=level,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, title, ippis_number, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            title=title,
            email=email,
            full_name=full_name,
            ippis_number=ippis_number,
            # department=department,
            gender=gender,
            password=password,
            **extra_fields
        )

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    LEVEL_CHOICES = (
    ('Level 1', 'Level 1'),
    ('Level 2', 'Level 2'),
    ('Level 3', 'Level 3'),
    ('Level 4', 'Level 4'),
    ('Level 5', 'Level 5'),
    ('Level 6', 'Level 6'),
    ('Level 7', 'Level 7'),
    ('Level 8', 'Level 8'),
    ('Level 9', 'Level 9'),
    ('Level 10', 'Level 10'),
    ('Level 11', 'Level 11'),
    ('Level 12', 'Level 12'),
    ('Level 13', 'Level 13'),
    ('Level 14', 'Level 14'),
    ('Level 15', 'Level 15'),
    ('Level 16', 'Level 16'),
    ('Level 17', 'Level 17'),
)

    TITLES = (
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
        ('Mr.', 'Mr.'),
        ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.'),
    )

    title = models.CharField(max_length=10, choices=TITLES)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    ippis_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'ippis_number'
    REQUIRED_FIELDS = ['full_name', 'title', 'email', 'gender']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Registered Users')
