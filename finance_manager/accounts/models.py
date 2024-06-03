from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class CustomUser(AbstractUser):
    # Add any additional fields if necessary
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Add related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"
