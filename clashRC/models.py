from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    college = models.CharField(blank=True, max_length=255)
    totalScore = models.IntegerField()


class Question(models.Model):
    quesTitle = models.CharField(max_length=255)
    quesDesc = models.TextField()
    sampleInput = models.TextField()
    sampleOutput = models.TextField()


class Submissions(models.Model):
    languages = [('c', 'C'), ('cpp', 'C++'), ('py', 'Python')]

    quesID = models.ForeignKey(Question, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    codeLang = models.CharField(max_length=3, choices=languages)
    # submittedCode = models.FilePathField
    # testResult = models.JSONField() or HStoreField (django.contrib.postgres required) or ArrayField --> TBD
    submissionTime = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
