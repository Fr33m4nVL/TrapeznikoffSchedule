from rest_framework import serializers
from django.contrib.auth import get_user_model

from schedule.models import *

# Schedule Serializers
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('__all__')

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('__all__')

class HomeworkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkComment
        fields = ('__all__')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('__all__')

# Users serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')