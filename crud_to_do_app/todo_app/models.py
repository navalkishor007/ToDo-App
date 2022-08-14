from django.db import models

# Create your models here.

class TodoData(models.Model):
    task_to_do = models.CharField(max_length=20)
    by_when_to_do = models.DateTimeField()

    def __str__(self):
        return f"%s: %s" %(self.id, self.task_to_do)
