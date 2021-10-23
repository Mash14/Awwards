from django.test import TestCase
from .models import Project

# Create your tests here.

class ProjectTestClass(TestCase):

    def setUp(self):
        self.new_project = Project(title = 'Club',image = 'image.png',description = 'A project about the quivers club',link = 'link.heroku.com')
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