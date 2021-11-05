from django.contrib import admin

# Register your models here.
from questions.models import Question, Profile, Tag

admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Tag)
