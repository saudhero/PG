from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username