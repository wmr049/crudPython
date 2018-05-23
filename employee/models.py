from django.db import models
from django.utils import timezone

class Emlpoyee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)        

    def __str__(self):
            return self.name