from django.urls import path

from .views import CategoriesALLView, CategoriesUpdateView, CategoriesDeleteView

urlpatterns = [
    path('', CategoriesALLView.as_view()),
    path('/<int:pk>', CategoriesUpdateView.as_view()),
    path('/<int:pk>', CategoriesDeleteView.as_view())
]
