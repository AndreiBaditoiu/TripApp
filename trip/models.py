from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return self.city


class Note(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')