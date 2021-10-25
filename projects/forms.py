from django import forms
from django.forms import fields
from .models import Profile,Project,Rates
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner','profile','pub_date']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['design', 'usability', 'content']