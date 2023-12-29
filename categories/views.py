from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from django_filters.rest_framework import DjangoFilterBackend

from .models import CategoriesModel
from .permissions import IsSuperuserOrReadOnly
from .serializers import CategoriesSerializer


class CategoriesALLView(ListCreateAPIView):
    parser_classes = (FileUploadParser,)
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class CategoriesUpdateView(UpdateAPIView):
    parser_classes = (FileUploadParser,)
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsSuperuserOrReadOnly,)


class CategoriesDeleteView(DestroyAPIView):
    parser_classes = (FileUploadParser,)
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsSuperuserOrReadOnly,)