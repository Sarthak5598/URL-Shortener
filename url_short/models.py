from django.db import models

# Create your models here.
class URL (models.Model):
    original_url=models.URLField(max_length=1000)
    short_url=models.CharField(max_length=100)
    created=models.DateField()
    
    def __str__(self) -> str:
        return f"{self.original_url} changed to {self.short_url}"