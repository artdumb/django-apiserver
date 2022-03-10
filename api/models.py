from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=50)


class Review(models.Model):
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
