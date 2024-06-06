from django.shortcuts import render
from .models import *
from rest_framework import generics
from . serializers import *

# Create your views here.

class BlogList(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
class BlogUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer    