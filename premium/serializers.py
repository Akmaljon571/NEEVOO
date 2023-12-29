from rest_framework.serializers import ModelSerializer

from .models import PremiumModel


class PremiumSerializer(ModelSerializer):
    class Meta:
        model = PremiumModel
        fields = '__all__'
        