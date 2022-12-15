from django.db import models


class Notes(models.Model):
    note_title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    snippet_title_01 = models.CharField(max_length=100, blank=True, default='')
    snippet_01 = models.TextField(blank=True)
    snippet_description_01 = models.TextField(blank=True)

    snippet_title_02 = models.CharField(max_length=100, blank=True, default='')
    snippet_02 = models.TextField(blank=True)
    snippet_description_02 = models.TextField(blank=True)

    snippet_title_03 = models.CharField(max_length=100, blank=True, default='')
    snippet_03 = models.TextField(blank=True)
    snippet_description_03 = models.TextField(blank=True)

    snippet_title_04 = models.CharField(max_length=100, blank=True, default='')
    snippet_04 = models.TextField(blank=True)
    snippet_description_04 = models.TextField(blank=True)

    def __str__(self):
        return self.note_title
