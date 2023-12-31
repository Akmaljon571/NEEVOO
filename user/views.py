from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.tokens import RefreshToken

from categories.models import CategoriesModel
from course.models import CourseModel
from video.models import VideoModel
from .pagination import CustomPageNumberPagination
from .serializers import *
from .utils import send_email


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        random = send_email(email)

        cache.set(random, {"email": email, "password": password})
        return Response({'message': "Send Email code"}, status=status.HTTP_200_OK)


class RegisterCodeView(CreateAPIView):
    serializer_class = RegistrationCodeSerializer

    def create(self, request, **kwargs):
        code = request.data.get('code')
        data = cache.get(code)
        if not data:
            return Response({'message': 'Code Invalid', "status": status.HTTP_400_BAD_REQUEST})

        serializer = RegistrationSerializer(data=data)
        if not serializer.is_valid():
            return Response({'message': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class PasswordEmailView(CreateAPIView):
    serializer_class = PasswordEmailSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        random = send_email(email)

        cache.set(random, {"email": email})
        return Response({'message': "Send Email code"}, status=status.HTTP_200_OK)


class PasswordCodeView(CreateAPIView):
    serializer_class = PasswordCodeSerializer

    def create(self, request, **kwargs):
        code = request.data.get('code')
        new_password = request.data.get('new_password')
        data = cache.get(code)
        user = request.user

        if not data:
            return Response({'message': 'Code Invalid', "status": status.HTTP_400_BAD_REQUEST})

        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)


class LoginView(CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                # If user is authenticated, generate JWT tokens
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(response_data, status=status.HTTP_200_OK)

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TokenRefreshView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate the refresh token
            RefreshToken(refresh_token)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        # If the refresh token is valid, generate a new access token
        new_access_token = RefreshToken(refresh_token).access_token

        return Response({'access_token': str(new_access_token)}, status=status.HTTP_200_OK)


class ListAdminView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['email']


class UserProfileDetail(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        serializer = UserLoginSerializer(request.user)
        return Response(serializer.data)


class HistoryCount(APIView):
    def get(self, request):
        categories = CategoriesModel.objects.all().count()
        courses = CourseModel.objects.all().count()
        videos = VideoModel.objects.all().count()
        users = User.objects.all().count()
        return Response({"yonalish": categories, "course": courses, "video": videos, "user": users})
