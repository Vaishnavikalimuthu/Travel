# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models

# class User(AbstractUser):
#     email = models.EmailField(unique=True)

#     # Resolve conflicts by setting related_name
#     groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']


from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo')