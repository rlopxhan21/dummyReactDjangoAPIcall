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
    
    
class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer  
    
    def perform_create(self, serializer):
            pk = self.kwargs['pk']
            ratingfield = Video.objects.get(pk=pk)
            serializer.save(assocvideo=ratingfield)
            
            
class RatingList(generics.ListAPIView):
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Rating.objects.filter(assocvideo=pk)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer