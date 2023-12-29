from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import PremiumModel
from .serializers import PremiumSerializer
from categories.permissions import IsSuperuserOrReadOnly


class PremiumAllView(ListCreateAPIView):
    queryset = PremiumModel.objects.all()
    serializer_class = PremiumSerializer
    permission_classes = (IsSuperuserOrReadOnly,)


class PremiumOneView(RetrieveUpdateDestroyAPIView):
    queryset = PremiumModel.objects.all()
    serializer_class = PremiumSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
