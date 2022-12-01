from django.db import models
from django.urls import reverse

# Create your models here.
class Feedback(models.Model):
    class Score(models.IntegerChoices):
        POOR = 1
        BAD = 2
        OK = 3
        GOOD = 4
        EXCELLENT = 5
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    score = models.IntegerField(choices=Score.choices)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('feedback_detail', args=[self.id])