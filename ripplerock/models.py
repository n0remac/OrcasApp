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
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    reason = models.TextField()
    life_quality = models.TextField()
    amenities = models.TextField()
    ideal_free_time = models.TextField()
    noncontentment = models.TextField()
    want_to_learn = models.TextField()
