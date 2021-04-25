from django.db import models

# Create your models here.
class Quiz(models.Model):
    '''
    This model is to store no of quizzes(different question set)
    '''
    quiz_name = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class QuestionAnswers(models.Model):
    '''
    This model is to store questions and answers for quiz (mapped with quiz)
    '''
    question = models.CharField(max_length=100)
    choice_1 = models.CharField(max_length=50)
    choice_2 = models.CharField(max_length=50)
    choice_3 = models.CharField(max_length=50)
    right_answer = models.CharField(max_length=50)
    marks = models.IntegerField()
    for_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE) 

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question_Answer"
        verbose_name_plural = "Questions_Answers"





