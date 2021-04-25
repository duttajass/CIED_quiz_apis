from rest_framework import serializers
from .models import Quiz, QuestionAnswers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','quiz_name']


class QuestionAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswers
        fields = ['id','question','choice_1','choice_2','choice_3','right_answer','marks','for_quiz']