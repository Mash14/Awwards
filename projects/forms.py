from django import forms
from .models import Profile,Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner','profile','pub_date']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']