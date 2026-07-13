from django.db import models

class Internship(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., June 2026 - Present")
    description = models.TextField()
    certificate = models.ImageField(upload_to='portfolio/certificates/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"