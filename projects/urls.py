from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home_page,name = 'homePage'),
    url('post/project/',views.post_project,name = 'post_project'),
    url('search/', views.search, name='search'),
    url('profile/',views.profile, name='profile_page'),
    url('profile/update/', views.update_profile, name='update_profile'),
    url('project/(?P<id>\d+)', views.single_project, name='view_project'),
    url('api/profile',views.ProfileList.as_view()),
    url('api/projects',views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)