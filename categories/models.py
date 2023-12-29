from django.db import models


class CategoriesModel(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title
