from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('play_quiz.urls')),
    path('get_or_add_quiz', views.get_or_add_quiz, name="get_or_add_quiz"),
    path('get_or_add_questions_for_quiz/<int:qid>', views.get_or_add_questions_for_quiz, name="get_or_add_questions_for_quiz"),
]