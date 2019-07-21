from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    url(r'^login/', auth_views.login, {'template_name':'userLogin.html'},name='login'),
    # url(r'login/profile', name='profile'),
    url(r'^logout/$', auth_views.logout),
    url(r'^signup/$',views.userSignup, name='user_register'),

]