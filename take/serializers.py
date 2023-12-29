from rest_framework.serializers import ModelSerializer

from .models import TakeModel


class TakeSerializer(ModelSerializer):
    class Meta:
        model = TakeModel
        fields = '__all__'
