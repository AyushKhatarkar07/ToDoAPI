from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    comp = models.BooleanField(default=False, blank = True, null = True)
    obj = models.Manager()

    # To print out an instance of Task model
    def __str__(self):
        return self.title
