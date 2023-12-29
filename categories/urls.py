from django.urls import path

from .views import CategoriesALLView, CategoriesUpdateView, CategoriesDeleteView

urlpatterns = [
    path('', CategoriesALLView.as_view()),
    path('update/<int:pk>/', CategoriesUpdateView.as_view()),
    path('delete/<int:pk>/', CategoriesDeleteView.as_view())
]
