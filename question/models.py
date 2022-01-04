from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    # tags = models.
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)





    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk' : self.pk})

class Answer(models.Model):
    body=models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Vote(models.Model):
    
    CHOICES = (
        ('upvote', 'upvote'),
        ('downvote', 'downvote'),
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.answer


class ExamQuestion(models.Model):
    image = models.ImageField(upload_to="question_images")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

