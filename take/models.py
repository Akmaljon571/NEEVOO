from django.db import models
from django.contrib.auth.models import User


class TakeModel(models.Model):
    month = models.IntegerField()
    price = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.month
    