from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from .serializers import *
from schedule.models import *

# Schedule Viewsets
class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

class HomeworkCommentViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkCommentSerializer
    queryset = HomeworkComment.objects.all()

class AnswerSerializer(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

# Users Viewsets
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
