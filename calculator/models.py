import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Text(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text