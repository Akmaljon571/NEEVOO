from django.db import models
from django.contrib.auth.models import User

from premium.models import PremiumModel


class TakeModel(models.Model):
    premium = models.ForeignKey(PremiumModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finish_date = models.DateField()
    create_at = models.DateField(auto_now_add=True)
