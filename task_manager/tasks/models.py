from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255, verbose_name='Задача')
    category = models.CharField(max_length=255, verbose_name='Категория')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.title