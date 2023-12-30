from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import TakeModel
from premium.serializers import PremiumSerializer


class TakeSerializer(ModelSerializer):
    class Meta:
        model = TakeModel
        fields = '__all__'


class TakeCreateSerializer(ModelSerializer):
    class Meta:
        model = TakeModel
        fields = ('premium', 'user',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active')


class TakeAdminSerializer(ModelSerializer):
    premium = PremiumSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = TakeModel
        fields = '__all__'
