from django.urls import path
from .views import TeachPage, download, SearchTeach

urlpatterns = [
    path('', TeachPage.as_view(), name="teach"),
    path('file/<pk>', download, name="downloadfile"),
    path('searchfile', SearchTeach.as_view(), name="searchfile"),
]