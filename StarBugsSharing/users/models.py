from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    email = models.EmailField(max_length=60, blank=False, unique=True)
    phone_number = models.CharField(max_length=20)
    balance_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    