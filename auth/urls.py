from django.urls import path, include
from .views import registerView, loginView, logoutUser

urlpatterns = [
    path('register/', registerView, name="register"),
    path('login/', loginView, name="login"),
    path('logout/', logoutUser, name="logout"),

]