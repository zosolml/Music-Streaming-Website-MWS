https://sharelatex.gwdg.de/project/6397abf971287b009a03e532





\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Abstract}
\author{Aditya Paul}
\date{December 2022}

\begin{document}



\maketitle




\section{Table of contents}:

1. Introduction

2. Chapter 1 - Console Commands

3. Chapter 2 - SDLC Life Cycle

4. Chapter 3 - MVT (Model View Template)

5. Chapter 4 - MVT Pipeline

6. Chapter 5 -Databases

\footnotesize{9}
\subsection{1. Introduction}:

The main objective of this project is to explore the features and capabilities of Django when coupled with html, css, and bootstrap. To do so we aim to build
a web application which is a music streaming website. The main views such as
songs and the list in case of music streaming websites respectively are updatable from the Django admin panel and We also create the facility to register,login and logout of these websites. And our templates will be configured to display messages such as passwords not matching and email already taken. Aditionally we also learn jinja format in this project which is a temptating language for python. We learn the uses of csrf-token, how to handle audio, picture files in this project. We also learn the process of automating the updatable views through the admin panel.

\subsection{Chapter 2 - Console Commands}:
:
When initializing the project we use the commands ” Django Admin Run
Project ” and ”Django admin create app” to run the server and to create new
apps for each project. We can use several apps for one project such as the
music app lifecycle for each project and another app for the next purpose. We
can use the commands such as ”Python manage.py make migrations” and ”
Python Manage.py migrate ” and ”Python manage.py remigrate” to update
the databases.
\subsection{ Chapter 3 - SDLC Life Cycle}:

The model we use is known as the waterfall model. The name is derived
from it is similarity to a cascade of waterfalls. In this model devolopers create
and test prototypes.This is repeated in each step. In our project there are 3
prototypes.In the first prototype we use js,css and html only to create a static
website. In the second prototype we actually implement Django into our project.
We make parts of the website dynamic in the second prototype. The third and
final prototype has translations and localization as an extra feature.
\subsection{ Chapter 4 - Model View Template}:

The Django website follows a (MVT) - Model View Template architecture.
The Models.py are forwarded to Views.py and then the Urls.py controls the
routing of the templates and forwards it to the html5 templates. We can source
the css files and use the ”href” and ” hkey ” to source the java script.

\subsection{ Chapter 5 - MVT Pipeline}:

models.py is a python file that uses classes with the modules kept in paren-
theses called models. Models and the Charfield is called verbose name which
states that this is a string or a float field that this is taken in to the views through the django admin panel and then pushed into the templates through
the databases. It is an update of the MVC architecture. To configure the
database for a single project we need to update the settings.py. For the
middlewares, templates, and static files root directory we have to configure
them in the settings.py too.




import os
import psycopg2
from django.utils.translation import gettext_lazy as-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(--file--)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q$p!f13)s0=jvr*#o#__n)+-sd9726y6!%1@m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED-APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',





]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT-URLCONF = 'music.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI-APPLICATION = 'music.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'music',
        'USER': 'postgres',
        'PASSWORD': 'asd123',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH-PASSWORD-VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE-CODE = 'en-us'

TIME-ZONE = 'UTC'

USE-I18N = True

USE-L10N = True

USE-TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC-URL = '/static/'
STATICFILES-DIRS=[
          os.path.join(BASE_DIR,'static')
          ]

STATIC-ROOT=os.path.join(BASE_DIR,'assests')

MEDIA-URL='/media/'
MEDIA-ROOT=os.path.join(BASE_DIR,'media/')
LOCALE-PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

After settings.py we will get forward the models.py to views.py to the templates and then urls.py is use to reroute the templates. 

\textbf{The Models.py are as follows which extends to views.py:}

from django.db import models


from django.utils import timezone
from django.urls import reverse
 
  
# Create your models here.
class song-thumb(models.Model):   
    artist=models.CharField(max_length=100,null=True)
    uploaded-by=models.CharField(max_length=100,null=True)
    song-title=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=250,null=True)
    album=models.CharField(max_length=100,null=True)            
    song_duration=models.FloatField(null=True)
    img=models.ImageField(upload_to='pics',null=True)
    song=models.FileField (upload_to='media',null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)


    def get-absolute-url(self):
        return reverse('song_detail',args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])




    class Meta:
        ordering = ('-publish',)
    def --str-(self):
        return self.song_title

class Comment(models.Model):
    post = models.ForeignKey(song_thumb,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null= True)
    updated = models.DateTimeField(auto_now= True, null= True)
    active = models.BooleanField(default=True)



\textbf{The models.py are as follows}:

from django.db import models

from django.utils import timezone
from django.urls import reverse

# Create your models here.
class song-thumb(models.Model):   
    artist=models.CharField(max-length=100,null=True)
    uploaded_by=models.CharField(max-length=100,null=True)
    song_title=models.CharField(max-length=100,null=True)
    slug=models.SlugField(max-length=250,null=True)
    album=models.CharField(max-length=100,null=True)            
    song_duration=models.FloatField(null=True)
    img=models.ImageField(upload-to='pics',null=True)
    song=models.FileField (upload-to='media',null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto-now_add=True)


    def get-absolute-url(self):
        return reverse('song_detail',args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])




    class Meta:
        ordering = ('-publish',)
    def --str--(self):
        return self.song_title

class Comment(models.Model):
    post = models.ForeignKey(song-thumb,
                             on-delete=models.CASCADE,
                             related-name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null= True)
    updated = models.DateTimeField(auto_now= True, null= True
    active = models.BooleanField(default=True)


\textbf{The views.py are as follows}:

from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import song_thumb,Comment
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import CommentForm
# Create your views here.

class SongListView(ListView):
    model=song_thumb
    context_object_name='posts'
    paginate_by=3
    template_name='songlist.html'

def song_detail(request, year, month, day, post):
    post = get_object_or_404(song_thumb, slug=post,

                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
            comment_form = CommentForm()
    return render(request,'musicplayer.html',{'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})



\textbf{ The urls.py are as follows}:


 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [

    path('',views.SongListView.as_view(),name='songs'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.song_detail,
         name='song_detail'),


]




\subsection{Chapter 6: Databases:}



The pseudocode of pgadmin4 will be configured into settings.py for the databases and the tables and coloumns will be generated.




(CREATE TABLE IF NOT EXISTS public.home-song-thumb
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    artist character varying(100) COLLATE pg_catalog."default",
    uploaded_by character varying(100) COLLATE pg-catalog."default",
    song-title character varying(100) COLLATE pg-catalog."default",
    slug character varying(250) COLLATE pg-catalog."default",
    album character varying(100) COLLATE pg-catalog."default",
    song-duration double precision,
    img character varying(100) COLLATE pg_catalog."default",
    song character varying(100) COLLATE pg_catalog."default",
    publish timestamp with time zone NOT NULL,
    created timestamp with time zone NOT NULL,
    CONSTRAINT home-song-thumb-pkey PRIMARY KEY (id)
)

TABLESPACE pg-default;

ALTER TABLE IF EXISTS public.home_song_thumb
    OWNER to postgres;
-- Index: home-song-thumb-slug-0357c5a0

-- DROP INDEX IF EXISTS public.home-song-thumb-slug-0357c5a0;

CREATE INDEX IF NOT EXISTS home-song-thumb-slug-0357c5a0
    ON public.home-song-thumb USING btree
    (slug COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg-default;
-- Index: home-song-thumb-slug-0357c5a0-like

-- DROP INDEX IF EXISTS public.home-song-thumb-slug-0357c5a0-like;

CREATE INDEX IF NOT EXISTS home-song-thumb-slug-0357c5a0-like
    ON public.home-song-thumb USING btree
    (slug COLLATE pg-catalog."default" varchar-pattern-ops ASC NULLS LAST)
    TABLESPACE pg-default;
\)\]

\end{document}