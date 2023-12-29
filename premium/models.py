from django.db import models


class PremiumModel(models.Model):
    type_title = models.CharField(max_length=255)
    month = models.IntegerField()
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.type_title
