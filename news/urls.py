from django.urls import path
from .views import NewsPage, NewsPageDetail

urlpatterns = [
    path('', NewsPage.as_view(), name="news"),
    path('<pk>/', NewsPageDetail.as_view(), name="newsdetail"),
]
