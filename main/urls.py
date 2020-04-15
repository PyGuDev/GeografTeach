from .views import MainView, AboutView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about")
]
