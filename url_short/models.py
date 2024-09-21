from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class URL (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    original_url=models.URLField(max_length=1000)
    short_code=models.CharField(max_length=100)
    created=models.DateTimeField()
     
    def __str__(self) -> str:
        return f"{self.original_url} changed to {self.short_code}"
    
class UserUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_reset = models.DateField(default=timezone.now().date())  # Store only the date
    usage_count = models.IntegerField(default=0)