from django.db import models

from categories.models import CategoriesModel


class CourseModel(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField()
    lang = models.CharField(max_length=10)
    description = models.TextField()
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
