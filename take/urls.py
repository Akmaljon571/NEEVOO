from django.urls import path

from .views import TakeAll, TakeDelete

urlpatterns = [
    path('', TakeAll.as_view()),
    path('<int:pk>/', TakeDelete.as_view())
]
