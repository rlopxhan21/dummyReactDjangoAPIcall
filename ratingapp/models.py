from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Video(models.Model):
    name = models.CharField(max_length=255)
    cast = models.CharField(max_length=1024)
    desc = models.CharField(max_length=1024)
    released = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    streamingplatform = models.ForeignKey('StreamingPlatform', on_delete=models.CASCADE, related_name='watchlist')
    avgrating = models.FloatField(default=0)
    totalrating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    rating_num = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    feedback = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    assocvideo = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='ratingfield')
    
    def __str__(self):
        return self.feedback