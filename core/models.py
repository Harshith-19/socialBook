from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.IntegerField()
    profile_image = models.ImageField(upload_to='profile_images',default='blank_profile.png')
    Bio = models.TextField(blank=True)
    location = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username


