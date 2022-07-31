from django.db import models
from django.utils import timezone

class Entry(models.Model):
    title = models.CharField(max_length=200)
    name= models.CharField(max_length=200 ,default='Gajendrasingh dawar')
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"