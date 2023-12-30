from django.db import models

from course.models import CourseModel


class VideoModel(models.Model):
    file = models.FileField()
    video_text = models.CharField(max_length=255)
    video_duration = models.CharField(max_length=255)
    sequence = models.IntegerField(unique=True)
    video_course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_text
