from rest_framework.serializers import ModelSerializer

from .models import VideoModel


class VideoSerializers(ModelSerializer):
    class Meta:
        model = VideoModel
        fields = "__all__"
