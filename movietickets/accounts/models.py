from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from PIL import Image

ROW=(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('G','G'),
    ('H','H')
)

SEATS=(
    ('s1','s1'),
    ('s2','s2'),
    ('s3','s3'),
    ('s4','s4'),
    ('s5','s5'),
    ('s6','s6'),
    ('s7','s7'),
    ('s8','s8'),
    ('s9','s9'),
    ('s10','s10')
)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)
    website=models.URLField(default='')
    #image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class Movie(models.Model):
    movie = models.CharField(max_length=150, default='')
    language=models.CharField(max_length=250,default='')
    sno = models.IntegerField(default=0)
    image = models.ImageField(upload_to='movie_image', blank=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")


class Theatre(models.Model):
    name=models.CharField(max_length=250,default='')
    city=models.CharField(max_length=250,default='')
    #seats=models.IntegerField(default=0)
    first=models.CharField(max_length=250,default='')
    second=models.CharField(max_length=250,default='')
    third=models.CharField(max_length=250,default='')
    #available=models.IntegerField(default=0)
    #booked=models.IntegerField(default=0)

    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name

class Book1(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    movie=models.CharField(max_length=250,default='')
    theatre=models.CharField(max_length=250,default='')
    show_time = datetime.datetime.now()
    show_number=models.CharField(max_length=250,default='')
    row= models.CharField(max_length=3, choices=ROW)
    column=models.CharField(max_length=4,choices=SEATS)
