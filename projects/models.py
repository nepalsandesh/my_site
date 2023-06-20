from django.db import models


class Project(models.Model):
    """Project database model"""
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ('-updated',)