from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if len(self.title) > 100:
            raise ValidationError("Title cannot exceed 100 characters.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
