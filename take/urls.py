from django.urls import path

from .views import TakeAdmin, TakeDelete, TakeCreate, TakeUser

urlpatterns = [
    path('admin/', TakeAdmin.as_view()),
    path('user/', TakeUser.as_view()),
    path('create/', TakeCreate.as_view()),
    path('delete/<int:pk>/', TakeDelete.as_view())
]
