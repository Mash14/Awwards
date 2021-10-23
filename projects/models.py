from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to = 'l_page/')
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=120)
    