from datetime import datetime
import hashlib
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('You must have an email')

        email = email.lower()
        first_name = first_name.title()
        last_name = last_name.title()

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        #user.password = password
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class CustomUser(AbstractBaseUser):
    RELIGION_CHOICE = (
        ('ISLAM', 'ISLAM'),
        ('HINDU', 'HINDU'),
        ('CHRISTIANITY', 'CHRISTIANITY'),
        ('OTHER', 'OTHER'),


    )

    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name_plural = "Users"

class EmailConfirmation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=500)
    email_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'User Email-Confirmed'


@receiver(post_save, sender=CustomUser)
def create_user_email_confirmation(sender, instance, created, **kwargd):
    if created:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance = EmailConfirmation(user=instance)
        user_encode = f'{instance.email}-{dt}'.encode()
        activation_key = hashlib.sha224(user_encode).hexdigest()
        email_confirmed_instance.activation_key = activation_key
        email_confirmed_instance.save()
