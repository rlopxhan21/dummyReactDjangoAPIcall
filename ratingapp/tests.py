from http.client import FORBIDDEN
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .api import serializers
from . import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
        
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", desc="#1 Platform")
    
    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "#1 Streaming platform",
            "website": "https://www.netflix.com"            
        }
        
        response = self.client.post(reverse('streamingplatform'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamingplatform'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('Streamingplatformdetail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamingplatform_put(self):
        response = self.client.put(reverse('Streamingplatformdetail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('Streamingplatformdetail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
class VideoListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
        
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", desc="#1 Platform")
        self.videolist = models.Video.objects.create(streamingplatform= self.stream, name= "The Salvation", cast= "Darius Tanz, Charlie Rowie", desc= "The movie about the astreoid poised to hit Earth by 171 days.", released= True)
    
    def test_videolist_create(self):
        data = {
            "streamingplatform": self.stream,
            "name": "The Salvation",
            "cast": "Darius Tanz, Charlie Rowie",
            "desc": "The movie about the astreoid poised to hit Earth by 171 days.",
            "released": True,
        }
        response = self.client.post(reverse('videolist'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_videolist_list(self):
        response = self.client.get(reverse('videolist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_Videolist_detail(self):
        response = self.client.get(reverse('videodetail', args=(self.videolist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_Videolist_delete(self):
        response = self.client.delete(reverse('videodetail', args=(self.videolist.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
class RatingTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
        
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", desc="#1 Platform")
        self.videolist = models.Video.objects.create(streamingplatform= self.stream, name= "The Salvation", cast= "Darius Tanz, Charlie Rowie", desc= "The movie about the astreoid poised to hit Earth by 171 days.", released= True)
        self.videolist1 = models.Video.objects.create(streamingplatform= self.stream, name= "The Salvationa", cast= "Darius Tanz, Charlie Rowie", desc= "The movie about the astreoid poised to hit Earth by 171 days.", released= True)

        
        self.review = models.Rating.objects.create(rating_num=5, feedback="On of the best movie in the century", author=self.user, assocvideo=self.videolist)

    def test_rating_create(self):
        data = {
            "rating_num": 5,
            "feedback": "Great Movie",
            "author": self.user,
            "assocvideo": self.videolist
        }
        
        response = self.client.post(reverse('rating-create', args=(self.videolist1.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.post(reverse('rating-create', args=(self.videolist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_rating_create_unauthenticated(self):
        data = {
            "rating_num": 5,
            "feedback": "Great Movie",
            "author": self.user,
            "assocvideo": self.videolist
        }
        
        self.client.force_authenticate(user=None)
        
        response = self.client.post(reverse('rating-create', args=(self.videolist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_rating_update(self):
        data = {
            "rating_num": 4,
            "feedback": "Great Movie -- updated",
            "author": self.user,
            "assocvideo": self.videolist
        }
        
        response = self.client.put(reverse('rating-create', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_rating_list(self):
        response = self.client.get(reverse('ratinglist', args=(self.videolist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_rating_delete(self):
        response = self.client.delete(reverse('ratingdetail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
