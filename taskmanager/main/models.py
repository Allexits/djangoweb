from django.db import models

class Task(models.Model):
    title = models.CharField('Name',max_length=50)
    desc = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Task Category'
        verbose_name_plural= 'Task Categories'