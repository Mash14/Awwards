from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to = 'l_page/')
    description = HTMLField()
    link = models.CharField(max_length=120)
