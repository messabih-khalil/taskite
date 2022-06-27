from email.policy import default
from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True , blank=True)
    user_name = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_name

class UserProfile(models.Model):
    user = models.OneToOneField(NewUser , on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, null=True , blank=True)
    email = models.EmailField()
    facebook = models.CharField(max_length=300 , null=True , blank=True)
    instagram = models.CharField(max_length=300 , null=True , blank=True)
    twitter = models.CharField(max_length=300 , null=True , blank=True)
    github = models.CharField(max_length=300 , null=True , blank=True)
    profile_image = models.ImageField(upload_to='profile_images' , default="default_profil.jpg")

    def __str__(self):
        return self.user.user_name

@receiver(post_save, sender=NewUser)
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user = instance , username = instance.user_name ,  email = instance.email)
        profile.save()