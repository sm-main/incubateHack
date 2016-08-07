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
    url(r'^profile-detail-page/$', 'general.views.profile_detail_page', name='profile_detail_page'),
    url(r'^all-blog/$', 'general.views.all_blog_page', name='all_blog_page'),
    url(r'^blog-detail-page/$', 'general.views.blog_detail_page', name='blog_detail_page'),
    url(r'^profile-detail-all-blog/$', 'general.views.profile_view_all_blog', name='profile_view_all_blog'),
    url(r'^act-now-page/$', 'general.views.act_now_page', name='act_now_page'),
    url(r'^community/$', 'general.views.community_view', name='community_view'),
    url(r'^community-single-page/$', 'general.views.community_single_page', name='community_single_page'),
    url(r'^all-notes/$', 'general.views.all_notes', name='all_notes')
]
