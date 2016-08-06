"""incubateHack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'general.views.home_page', name='home_page'),
    url(r'^sign-up-page2/$', 'general.views.sign_up_page2', name="sign_up_page2"),
    url(r'^profile-edit/$', 'general.views.profile_edit_page', name='profile_edit_page'),
    url(r'^all-blog/$', 'general.views.all_blog_page', name='all_blog_page')
]
