from django.db import models

# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimestampModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    