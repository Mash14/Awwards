from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTestClass(TestCase):

    def setUp(self):
        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

        self.new_profile = Profile(profile_pic = 'image3.jpg', bio = 'G.O.A.T', contact = '0791919191',user = self.user)
        self.new_profile.save()

        self.new_project = Project(title = 'Club',image = 'image.png',description = 'A project about the quivers club',link = 'link.heroku.com',profile=self.new_profile)
        self.new_project.save_project()

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.new_project.save_project()
        self.new_project.delete_project(id = self.new_project.id)
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

    def test_search_method(self):
        self.new_project.save_project()
        title = 'Club'
        searched_projects = self.new_project.search_project(title)
        self.assertTrue(len(searched_projects)>0)

    def test_get_project_by_id(self):
        self.new_project.save_project()
        search_project = self.new_project.get_project_by_id(self.new_project.id)
        searched_project = Project.objects.filter(id=self.new_project.id)
        self.assertTrue(searched_project,search_project)