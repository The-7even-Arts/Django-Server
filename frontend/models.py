from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Article(models.Model):
    image               = CloudinaryField('Teksolutions/Articles/Images/', default="Teksolutions/Articles/Images/default.png")
    headline            = models.CharField(max_length=200)
    short_description   = models.CharField(max_length=200)
    
    body                = models.TextField()
    
    tags                = models.CharField(max_length=200)
    likes               = models.IntegerField(default=0)
    slug                = models.SlugField(blank=True)
    
    def __str__(self):
        return self.headline
    
    def save(self, *args, **kwargs):
        if len(self.slug) < 1:
            self.slug = slugify(self.headline)
            self.save()
            
        return super().save(*args, **kwargs)
    
    