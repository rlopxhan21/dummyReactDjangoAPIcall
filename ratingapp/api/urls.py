from django.urls import path, include

from .views import RatingDetail, VideoList, VideoDetail, StreamingPlatformList, StreamingPlatformDetail

urlpatterns = [
    path('video/', VideoList.as_view(), name='videolist'),
    path('video/<int:pk>/', VideoDetail.as_view(), name='videodetail'),
    
    path('sp/', StreamingPlatformList.as_view(), name='streamingplatform'),
    path('sp/<int:pk>/', StreamingPlatformDetail.as_view(), name='Streamingplatformdetail'),
    
    # path('video/<int:pk>/rating-create/', RatingCreate.as_view(), name='rating-create'),
    # path('video/<int:pk>/rating/', RatingList.as_view(), name='ratinglist'),
    path('video/rating/<int:pk>/', RatingDetail.as_view(), name='ratingdetail'),
]