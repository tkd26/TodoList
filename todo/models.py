from django.db import models

# Create your models here.

PRIORITY = (('high', 'high'), ('normal', 'normal'), ('low', 'low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY,
        default = 'high',
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
