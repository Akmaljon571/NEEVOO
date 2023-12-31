from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from video.models import VideoModel
from .models import CourseModel
from .serializers import CourseSerializer, CourseAllSerializer
from categories.permissions import IsSuperuserOrReadOnly
from categories.models import CategoriesModel


class CourseAllView(APIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    serializer_class = CourseAllSerializer
    queryset = CourseModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def get(self, request, *args, **kwargs):
        courses = CourseModel.objects.all()
        serialized_courses = CourseAllSerializer(courses, many=True).data

        for course_data in serialized_courses:
            course_id = course_data['id']
            videos_count = VideoModel.objects.filter(video_course=course_id).count()
            course_data['video_count'] = videos_count

        return Response(serialized_courses)


class CourseCreateView(CreateAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()


class CourseUpdateView(UpdateAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    parser_classes = (FileUploadParser,)


class CourseDeleteView(DestroyAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    parser_classes = (FileUploadParser,)


class ByCategories(APIView):
    def get(self, request, category_id):
        try:
            category = CategoriesModel.objects.get(pk=category_id)
            courses = CourseModel.objects.filter(category=category)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except CategoriesModel.DoesNotExist:
            return Response(data={'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
