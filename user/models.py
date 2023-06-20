from django.db import models
from projects.models import Project

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, null=True, default="Anonymous")
    bio = models.TextField()
    passion = models.TextField()
    profile_picture = models.ImageField(upload_to='media/images', null=True)
    
    def __str__(self):
        return str(self.name)


