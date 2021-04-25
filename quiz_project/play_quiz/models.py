from django.db import models
from quiz_questions.models import Quiz

# Create your models here.
class Play(models.Model):
    user_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f'user: {self.user_name}, score: {self.score}'
