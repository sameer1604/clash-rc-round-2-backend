from django.contrib import admin
from .models import Profile, Question, Submissions
myModels = [Profile, Question, Submissions]
admin.site.register(myModels)

