from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Survey(models.Model):
    time_on_island = models.CharField(max_length=200, blank=True, null=True, default='0 - 1')
    age = models.IntegerField(blank=True, null=True, default=' ')
    reason = models.TextField(blank=True, null=True, default=' ')
    life_quality = models.TextField(blank=True, null=True, default=' ')
    amenities = models.TextField(blank=True, null=True, default=' ')
    ideal_free_time = models.TextField(blank=True, null=True, default=' ')
    noncontentment = models.TextField(blank=True, null=True, default=' ')
    want_to_learn = models.TextField(blank=True, null=True, default=' ')


class Paragraph(models.Model):
    paragraph = models.TextField(blank=True, null=True, default=' ')
    page = models.CharField(max_length=50, null=True, default=' ')