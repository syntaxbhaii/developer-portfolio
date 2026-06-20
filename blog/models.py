from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # The slug is the URL-friendly version of the title
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(help_text="Write your article here.")
    thumbnail = models.ImageField(upload_to='blog/thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title if it doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at'] # Shows newest posts first