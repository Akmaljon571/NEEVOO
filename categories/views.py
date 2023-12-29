from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission
from django_filters.rest_framework import DjangoFilterBackend

from .models import CategoriesModel
from .serializers import CategoriesSerializer


class IsSuperuserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        return request.user and request.user.is_superuser


class CategoriesALLView(ListCreateAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class CategoriesOneView(RetrieveUpdateDestroyAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
