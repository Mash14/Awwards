from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'l_page/')
    bio = HTMLField()    
    contact = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id = id).delete()
        
class Project(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to = 'l_page/')
    description = HTMLField()
    link = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def delete_project(cls,id):
        cls.objects.filter(id = id).delete()

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls,id):
        projects = cls.objects.get(id = id)
        return projects

class Rates(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    usability = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    content = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    average = models.DecimalField(default=1, blank=False, decimal_places=2, max_digits=40)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title