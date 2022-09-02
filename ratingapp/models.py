from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    cast = models.CharField(max_length=1024)
    desc = models.CharField(max_length=1024)
    released = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    streamingplatform = models.ForeignKey('StreamingPlatform', on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return self.name
    
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    feedback = models.CharField(max_length=1024)
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    assocvideo = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='ratingfield')
    
    def __str__(self):
        return self.feedback