from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    cast = models.CharField(max_length=1024)
    desc = models.CharField(max_length=1024)
    released = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

        
    