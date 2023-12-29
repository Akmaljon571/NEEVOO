from django.urls import path

from .views import CategoriesALLView, CategoriesOneView

urlpatterns = [
    path('', CategoriesALLView.as_view()),
    path('/<int:pk>', CategoriesOneView.as_view())
]
