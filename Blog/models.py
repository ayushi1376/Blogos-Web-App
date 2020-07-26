from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField(default=None)
    author=models.CharField(max_length=13)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author

class Blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(blank=True)
