from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HomeworkSerializer
from .models import Homework

class HomeworkView(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
