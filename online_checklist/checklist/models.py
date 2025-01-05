from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now


# Custom user manager to create and manage users
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


# CustomUser class (based on AbstractUser)
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assign the custom user manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username


# UserProfile linked to the custom user model
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Use the custom user model
        on_delete=models.CASCADE   # Specify the behavior on delete
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,13}$',
                message="Phone number must be entered in the format: '+254712345678'. Up to 13 digits allowed."
            )
        ]
    )

    def __str__(self):
        return self.user.username





class ChecklistItem(models.Model):
    title = models.CharField(max_length=200, default="Enter Name")
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,13}$',
                message="Phone number must be entered in the format: '+254712345678'. Up to 13 digits allowed."
            )
        ]
    )
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
