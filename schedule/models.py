from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    SUBJECT_COLORS = [
        (1, 'Gray'),
        (2, 'Red'),
        (3, 'Yellow'),
        (4, 'Green'),
        (5, 'Blue'),
        (6, 'Indigo'),
        (7, 'Purple'),
        (8, 'Pink'),
    ]
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=50, blank=True, null=True)
    color = models.IntegerField( blank=True, null=True, choices=SUBJECT_COLORS)

    def __str__(self):
        return self.name

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class HomeworkComment(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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