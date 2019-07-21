Inside dir of the project created webapp dir named -skillportal_web:

In cmd from this dir:

django-admin startproject skillportal

python manage.py startapp cv_app  //creation of app

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

//superuser: liza
//pwd: lizaliza

python manage.py runserver

Add your app name in skillportal/settings.py INSTALLED APPS:

INSTALLED APPS:[
    ...
    ...,
    'cv_app',

]

For LOGIN:

Add in skillportal/urls.py :

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]

//alternatively urls can be added thru' app/urls.py --explained later below.

Then on settings.py -> change in templates: add html templates here

'DIRS': ['templates'],
//its the path for templates - since templates created in root dir so only written templates

Create base template of own to extend to other template.

Create registration folder inside templates and create login template nad extend base.html to this template

Edit in cv_app/views.py to display the homepage like:

from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, This is my first blog!!")
    return render(request, 'homepage.html')

def homepage(request):
    return render(request, 'login.html')

//here let login.html be the homepage for now.

Also create urls.py in app i.e. cv_app -> urls.py
it is for all our app urls like:

//You can also add login like this to app/urls.py :

//Use 127.1.0.0:8000/skillportal/login

In cv_app/urls.py add :

from django.contrib.auth import views as auth_views

Add In urlpatterns:

url(r'^login/$', auth_views.login, {'template_name':'login.html'},name='login'),
url(r'^logout/$', auth_views.logout, {'template_name':'logout.html'},name='logout'),

like this:

from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name ='homepage'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'logout.html'},name='logout'),
]

//If directly 127.1.0.0:8000/login then add to skillportal/urls.py

//here views.index is default 1st page
// inside views.py we create def(homepage) and other function for urls

//and then add this url path to project urls.py file like:

path('skillportal/',include('cv_app.urls')),

//here skillportal is root dir and cv.urls is the urls.py created file

//Also to add static files:

//create in root dir i.e. skillportal static folder and in that add css and js files.

In main skillportal/urls.py add:

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	<..all urls>
] + staticfiles_urlpatterns()

In your settings, you should have:

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")		//required only in deployment

# Add to settings.py - Make a tuple of strings instead of a string
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static/'),
]
//where static is the dir for storing static files newly created under root dir and thiis done automatically during runserver


Create css/media or diff subdirectory to handle files of static:
Eg: static/css/style.css

Write style.css and add in templates/eg.html like this:

{% load staticfiles %}		//add this block for django
<link rel="stylesheet" type="text/css" href="{% static "css/style.css" %}">

#For bootstrap:

pip install django-crispy-forms         //if not installed

In settings.py:

INSTALLED_APPS = [
    ...

    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4

Setup bootstrap:

Can download from getbootstrap.com. Or you can use the hosted Bootstrap CDN:

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

In this -> for using bootstrap:

In html code -> these added in head:

        <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
        <script type="text/javascript" src="jquery-3.3.1.slim.min.js"></script>
        <script type="text/javascript" src="bootstrap.min.js"></script>


To navigate from one page to another in django:

{% url 'some-url-name' v1 v2 %}

like done in index.html:

<a href="{% url 'login' %}" >USER LOGIN <br><span id="q">click here</span></a>

//here 'login' is the name of url that can be found in app/urlpatterns in the project.

#FORMS:

create forms.py:

from django import forms

//then create class for respective form with required fields.like:

class UserLoginForm(forms.Form):
    user =forms.CharField(max_length = 100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

//Create html form.like: userLogin.html

In action: write the url for action page. like:

<form name = "form" action = "{% url "login" %}" method = "POST" >
      {% csrf_token %}

//here to prevent Cross-site Request Forgery (CSRF) attack on your site.
{% csrf_token %} tag is used for every form.

//In views.py : create function to request, validate and return form.
//then add in url

from django.contrib.auth import views as auth_views

url(r'^login/', auth_views.login, {'template_name':'userLogin.html'},name='login'),


//Phone field in django

pip install django-phone-field

//Then add 'phone_field' to INSTALLED_APPS in settings.py

//Usage:

//In models.py/forms.py wherever you need:

from phone_field import PhoneField

class ...(..):
    phone = PhoneField(blank=True, help_text='Contact Number')

PhoneField accepts standard options for a Django CharField. By default it sets max_length=31. Feel free to override this, set blank=True, etc. as you would otherwise.

There is one special argument, E164_only=False, which adds a form validator to only accept numbers in the E164 format (currently, only supported for US phone numbers).
In your template:

User {{ obj.name }} has phone number {{ obj.phone }}
Result:

User Ted has phone number (415) 123-1233

//Database representation
PhoneField attempts to coerce all phone numbers to the following format:

+[country code][number]x[extension]
+12223334444x55
where the extension part is optional. If the input phone number can't be coerced to this format, PhoneField gives up and simply stores it as-is.

Because all phone numbers are stored without formatting, you can set this field to be unique on a Django model and it will actually work.

Or regex pattern used for Nepal:

pattern = " (\+977)?\d{10}"

For Password Confirmation:  js code added in signup html form


DATABASE:

//In settings.py: edit according to your database like for MySQL,Oracle etc.,add parameters acc to need like: username,pwd, host
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

//Creating Models
.... notes left to write
....

//After creating models - for models do migrations
//for db creation - in case of sqlite

python manage.py makemigrations
python manage.py migrate


//for MySQL, oracle need to create table by own on their platforms

