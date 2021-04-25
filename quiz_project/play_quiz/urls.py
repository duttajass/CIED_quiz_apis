from django.urls import path
from . import views

urlpatterns = [
    path('get_or_add_play', views.get_or_add_play, name="get_or_add_play"),
    path('get_play_details/<int:pid>', views.get_play_details, name="get_play_details"),
    path('submit_quiz/<int:pid>', views.submit_quiz, name="submit_quiz"),
]