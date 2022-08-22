import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.IntegerField()
    profile_image = models.ImageField(upload_to='profile_images', default='blank_profile')
    Bio = models.TextField(blank=True)
    location = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user
