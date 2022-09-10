from django.contrib import admin

from .models import Video, StreamingPlatform, Rating


admin.site.register(Video)
admin.site.register(StreamingPlatform)
admin.site.register(Rating)
