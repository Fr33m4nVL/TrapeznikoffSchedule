from django.contrib import admin
from schedule.models import Subject, Homework, HomeworkComment, Answer

admin.site.register(Subject)
admin.site.register(Homework)
admin.site.register(HomeworkComment)
admin.site.register(Answer)