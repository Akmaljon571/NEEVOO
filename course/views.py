from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CourseModel
from .serializers import CourseSerializer
from categories.permissions import IsSuperuserOrReadOnly
from categories.models import CategoriesModel


class CourseAllView(ListCreateAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    parser_classes = (FileUploadParser,)


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
