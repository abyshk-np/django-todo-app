

from time import timezone

from django.db import models

# Create your models here.
class Todo(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()
    date = models.DateField(default=True)
    completed=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.tittle
