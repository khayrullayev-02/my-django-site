from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
