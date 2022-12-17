from django.db import models


def user_directory_path(instance, filename):
    return f'user/{filename}'

class Contact(models.Model):
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    twitter_handle = models.CharField(max_length=250, blank=True)
    avatar_url = models.TextField(blank=True)
    avatar_image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    favorite = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ['created']
