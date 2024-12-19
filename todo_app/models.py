from django.db import models


class TodoTask(models.Model):
    title = models.CharField(max_length=100, unique=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
