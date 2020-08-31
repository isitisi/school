from django.shortcuts import render
from rest_framework import generics
from .models import flowers
from .serializers import FlowersSerializers

class ListFlowers(generics.ListCreateAPIView):
    queryset = flowers.objects.all()
    serializer_class = FlowersSerializers

class DetailFlowers(generics.RetrieveUpdateDestroyAPIView):
    queryset = flowers.objects.all()
    serializers_class = FlowersSerializers

# Create your views here.
# def index(request):
#     return render(request,'index.html')
