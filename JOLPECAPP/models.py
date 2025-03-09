from django.db import models
from django.db.models import Model 


# Create your models here.
class EjecsModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    logo = models.ImageField(default='fallback.png', blank=True)
    
    
    def __str__(self):
        return self.title