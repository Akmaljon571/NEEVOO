from django.urls import path

from .views import VideoCreateView, VideoDeleteView, VideoUpdateView

urlpatterns = [
    path('create/', VideoCreateView.as_view()),
    path('update/<int:pk>/', VideoUpdateView.as_view()),
    path('delete/<int:pk>/', VideoDeleteView.as_view()),
]
