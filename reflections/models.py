from django.db import models


class Configuration(models.Model):
    create_date = models.DateField("date created")


class Question(models.Model):
    question_text = models.CharField()
    sort_index = models.IntegerField(default=0)
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)


class Reflection(models.Model):
    create_date = models.DateField("reflection date")
    questions = models.ManyToManyField(
        Question, through="Answer", through_fields=("reflection", "question")
    )


class Answer(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
