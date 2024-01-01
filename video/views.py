from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from .models import VideoModel
from .serializers import VideoSerializers
from take.models import TakeModel
from take.serializers import TakeSerializer


class VideoAllView(APIView):
    def get(self, request, pk):
        user_id = request.user.id
        print(request.user)
        videos = VideoModel.objects.filter(video_course=pk)
        serializer = VideoSerializers(videos, many=True)
        serialized_data = serializer.data

        allTakes = TakeModel.objects.filter(user=user_id)
        if not len(allTakes):
            for video in serialized_data:
                video['file'] = ''
            return Response({"status": False, "data": serialized_data})

        take_serializer = TakeSerializer(allTakes, many=True)
        take_data = take_serializer.data
        day = datetime.now()
        take_result = []
        for take in take_data:
            date_s = '.'.join(dict(take)['finish_date'].split('-')[::-1])
            finish_date = datetime.strptime(date_s, '%d.%m.%Y')
            take_result.append(finish_date > day)

        if not all(take_result):
            for video in serialized_data:
                video['file'] = ''
            return Response({"status": False, "data": serialized_data})

        return Response({"status": True, "data": serialized_data})


class VideoOneView(APIView):
    def get(self, request, pk):
        user_id = request.user.id
        try:
            video_one = VideoModel.objects.get(id=pk)
        except VideoModel.DoesNotExist:
            return Response({"message": "Video Not Found", "status": status.HTTP_404_NOT_FOUND})

        video = VideoSerializers(video_one).data

        allTakes = TakeModel.objects.filter(user=user_id)
        if not len(allTakes):
            video['file'] = ''
            return Response({"status": False, "data": video})

        take_serializer = TakeSerializer(allTakes, many=True)
        take_data = take_serializer.data
        day = datetime.now()
        take_result = []
        for take in take_data:
            date_s = '.'.join(dict(take)['finish_date'].split('-')[::-1])
            finish_date = datetime.strptime(date_s, '%d.%m.%Y')
            take_result.append(finish_date > day)

        if not all(take_result):
            video['file'] = ''
            return Response({"status": False, "data": video})

        return Response({"status": True, "data": video})


class VideoCreateView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
    parser_classes = (FileUploadParser,)


class VideoAdminAllView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, course):
        video_data = VideoModel.objects.filter(video_course=course)
        video = VideoSerializers(video_data, many=True).data
        return Response({"data": video})


class VideoUpdateView(UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
    parser_classes = (FileUploadParser,)


class VideoDeleteView(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializers
