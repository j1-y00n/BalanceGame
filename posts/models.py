from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=80)
    select1_content = models.CharField(max_length=200)
    select2_content = models.CharField(max_length=200)
    image1 = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image2 = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    select1_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='select1_posts')
    select2_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='select2_posts')
