from rest_framework import serializers
from django.contrib.auth import get_user_model


class RegistrationCodeSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = ('code',)


class PasswordCodeSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()
    new_password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('code', 'new_password')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['email'],
            password=validated_data['password']
        )
        return user


class PasswordEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
