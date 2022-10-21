from django.db import models

# Create your models here.
# 파이썬에서는 상속 개념 사용
# models.Model을 통해 상속 가능하도록 해줌
# 자동으로 id 값 만들어 줌

class Question(models.Model):
    question_txt = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_txt

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt