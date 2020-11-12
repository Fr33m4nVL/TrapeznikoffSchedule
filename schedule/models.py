from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    #teacher

    def __str__(self):
        return self.name

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    hand_over_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
 
class HomeworkComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:30] + "..."

class Answer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:30] + "..."