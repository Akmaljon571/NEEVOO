from django.urls import path

from .views import *

urlpatterns = [
    path('course/<int:pk>', VideoAllView.as_view()),
    path('one/<int:pk>', VideoOneView.as_view()),
    path('admin/<int:course>', VideoAdminAllView.as_view()),
    path('create/', VideoCreateView.as_view()),
    path('update/<int:pk>/', VideoUpdateView.as_view()),
    path('delete/<int:pk>/', VideoDeleteView.as_view()),
]
