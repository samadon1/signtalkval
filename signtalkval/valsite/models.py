from django.db import models

# Create your models here.

from django.db import models


class Data(models.Model):
    filename = models.CharField(max_length = 200)
    url = models.URLField()
    isCorrect = models.BooleanField()
    correctText = models.CharField(max_length = 200)

    def __str__(self):
        return self.filename
    
    