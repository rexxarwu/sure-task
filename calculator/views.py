from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TextSerializer
from .models import Text


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('text')
    serializer_class = TextSerializer

def index(request):
    return render(request, 'calculator/index.html')
