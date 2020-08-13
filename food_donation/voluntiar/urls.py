from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name = 'Login_Voluntiar'),
]