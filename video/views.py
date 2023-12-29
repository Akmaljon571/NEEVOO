from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from .models import VideoModel
from .serializers import VideoSerializers


class VideoCreateView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
    parser_classes = (FileUploadParser,)


class VideoUpdateView(UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
    parser_classes = (FileUploadParser,)


class VideoDeleteView(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
