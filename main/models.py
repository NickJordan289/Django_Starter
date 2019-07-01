from django.db import models
from django.contrib.auth.models import User


class UserExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def approve(self):
        self.save()

    def __repr__(self):
        return f"users('{self.user.get_full_name()}', '{self.user.email}, '{self.role.name}')"