from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()

