from django.contrib import admin
from django.urls import path
from .views import LoginView,RegisterView,LoggedInPageView

urlpatterns = [
    path('', LoginView, name="login"),
    path('register/', RegisterView, name="register"),
    path('loggedinpage/', LoggedInPageView, name="loggedinpage"),
]
