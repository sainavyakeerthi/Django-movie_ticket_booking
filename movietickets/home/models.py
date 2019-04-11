from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    language=models.CharField(max_length=150)
    location=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    date=models.DateTimeField(auto_now=True)
    theator=models.CharField(max_length=250)