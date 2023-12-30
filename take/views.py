from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

from .models import TakeModel
from .serializers import TakeSerializer, TakeAdminSerializer, TakeCreateSerializer
from premium.models import PremiumModel
from premium.serializers import PremiumSerializer


class TakeAdmin(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TakeAdminSerializer
    queryset = TakeModel.objects.all()


class TakeUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TakeSerializer

    def get(self, request):
        findTakes = TakeModel.objects.filter(user=request.user)
        if not len(findTakes):
            return Response(data='User Take Not Found', status=status.HTTP_404_NOT_FOUND)
        take = TakeSerializer(findTakes, many=True)
        data = []
        for i, a in enumerate(take.data):
            pre = PremiumModel.objects.get(pk=dict(a)['premium'])
            premium = PremiumSerializer(pre).data
            date_s = '.'.join(dict(a)['finish_date'].split('-')[::-1])
            date_object = datetime.strptime(date_s, '%d.%m.%Y')
            data.append({
                "title": premium['type_title'],
                "create_date": '.'.join(dict(a)['create_at'].split('-')[::-1]),
                "price": premium["price"],
                "active": date_object > datetime.now(),
                "finish_date": date_s,
            })
        return Response(data)


class TakeCreate(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TakeCreateSerializer

    def post(self, request):
        premium_id = request.data["premium"]
        user_id = request.data['user']
        day = datetime.now()

        premium = PremiumModel.objects.get(pk=premium_id)
        finish_date = day + timedelta(premium.month*30)

        data = {
            "premium": premium_id,
            "user": user_id,
            "finish_date": finish_date.strftime("%Y-%m-%d")
        }
        serializer = TakeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data successfully processed'}, status=status.HTTP_201_CREATED)
        return Response(data={'message': 'Take data BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


class TakeDelete(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TakeSerializer
    queryset = TakeModel.objects.all()
