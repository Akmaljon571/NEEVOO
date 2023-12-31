from django.urls import path

from .views import CourseDeleteView, CourseUpdateView, CourseAllView, ByCategories, CourseCreateView

urlpatterns = [
    path('', CourseAllView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('update/<int:pk>/', CourseUpdateView.as_view()),
    path('delete/<int:pk>/', CourseDeleteView.as_view()),
    path('<int:category_id>/', ByCategories.as_view()),
]
