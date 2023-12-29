from django.urls import path

from .views import PremiumOneView, PremiumAllView

urlpatterns = [
    path('', PremiumAllView.as_view()),
    path('<int:pk>', PremiumOneView.as_view())
]
