from django.shortcuts import render
# from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def sign_up_page2(request):
    return render(request, 'sign_up_page2.html')

def profile_edit_page(request):
    return render(request, 'profile_edit.html')

def all_blog_page(request):
    active_all_blog = True
    context = {'active_all_blog':active_all_blog}
    return render(request, 'all_blog_page.html', context)

def blog_detail_page(request):
    return render(request, 'blog_detail_page.html')

def profile_detail_page(request):
    return render(request, 'profile_detail_page.html')

def profile_view_all_blog(request):
    return render(request, 'all_blog_page.html')

def act_now_page(request):
    return render(request, 'act_now_page.html')

def community_view(request):
    active_community = True
    context = {'active_community':active_community}
    return render(request, 'community_view.html', context)

def webinar_view(request):
    active_webinar = True
    context = {'active_webinar':active_webinar}
    return render(request, 'webinar_view.html', context)

def events_view(request):
    active_events = True
    context = {'active_events':active_webinar}
    return render(requset, 'events_view.html', context)


def community_single_page(request):
    return render(request, 'community_single_page.html')

def all_notes(request):
    return render(request, 'all_notes.html')
