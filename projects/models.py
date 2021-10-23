from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to = 'l_page/')
    description = HTMLField()
    link = models.CharField(max_length=120)

    def save_project(self):
        self.save()

    @classmethod
    def delete_project(cls,id):
        cls.objects.filter(id = id).delete()

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects