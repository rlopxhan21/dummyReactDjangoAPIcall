# from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from ratingapp.models import Video, StreamingPlatform, Rating
from .serializers import VideoSerializer, StreamignPlatformSerializer, RatingSerializer
from ratingapp.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from .throttling import ReviewCreateThrottle, ReviewListThrottle
from .pagination import VideoListPagination, VideoListLOPagination, VideoListCPagination


class UserRatingList(generics.ListAPIView):
    serializer_class = RatingSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Rating.objects.filter(author__username=username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Rating.objects.filter(author__username=username)


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminOrReadOnly]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=name', 'desc']
    pagination_class = VideoListCPagination
    
class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminOrReadOnly]


class StreamingPlatformList(generics.ListCreateAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamignPlatformSerializer
    permission_classes = [AdminOrReadOnly]
    
    
class StreamingPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamignPlatformSerializer
    permission_classes = [AdminOrReadOnly]
    

class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

    
    def get_queryset(self):
        return Rating.objects.all() 
    
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        videolist = Video.objects.get(pk=pk)
        queryset = Rating.objects.filter(assocvideo=videolist, author=self.request.user)
        if queryset.exists():
            raise ValidationError("You have already reviews this video!")
        
        if videolist.totalrating == 0:
            videolist.avgrating = serializer.validated_data['rating_num']
        else:
            videolist.avgrating = (videolist.avgrating + serializer.validated_data['rating_num'])/2
        
        videolist.totalrating = videolist.totalrating + 1
        videolist.save()
        
        serializer.save(assocvideo_id=pk, author=self.request.user)
            

class RatingList(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__username', 'assocvideo__name']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        videolist = Video.objects.get(pk=pk)
        return Rating.objects.filter(assocvideo=videolist)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [ReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    

