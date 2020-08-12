from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'food_donation'),
    path('register', views.register, name='registration'),
    path('profile', views.profile, name='profile'),

]
