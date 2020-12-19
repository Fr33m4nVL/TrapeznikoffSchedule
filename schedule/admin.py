from django.contrib import admin
from schedule.models import Subject, Homework, HomeworkComment, Answer

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject')

class HomeworkCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(HomeworkComment, HomeworkCommentAdmin)
admin.site.register(Answer, AnswerAdmin)