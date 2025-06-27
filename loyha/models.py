from django.db import models

class Loyha(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='loyha/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.title
