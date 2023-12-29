from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import TakeModel
from .serializers import TakeSerializer


class TakeAll(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TakeSerializer
    queryset = TakeModel.objects.all()


class TakeDelete(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TakeSerializer
    queryset = TakeModel.objects.all()
