from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Images will be uploaded to media/portfolio/images/
    image = models.ImageField(upload_to='portfolio/images/')
    github_url = models.URLField(blank=True, help_text="Link to source code")
    live_url = models.URLField(blank=True, help_text="Link to live demo (if any)")
    technologies = models.CharField(max_length=200, help_text="E.g., Django, Python, Bootstrap")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at'] # Shows newest projects first