from rest_framework.serializers import ModelSerializer

from .models import CategoriesModel


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = "__all__"
