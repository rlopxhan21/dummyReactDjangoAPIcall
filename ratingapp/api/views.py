# from rest_framework.response import Response
from rest_framework import generics

from ratingapp.models import Video, StreamingPlatform, Rating
from .serializers import VideoSerializer, StreamignPlatformSerializer, RatingSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    
class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class StreamingPlatformList(generics.ListCreateAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamignPlatformSerializer
    
    
class StreamingPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamignPlatformSerializer
    
    




class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer