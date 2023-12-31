from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import CourseModel
from video.serializers import VideoSerializers


class CourseSerializer(ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"


class CourseAllSerializer(ModelSerializer):
    videos = VideoSerializers(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = '__all__'
