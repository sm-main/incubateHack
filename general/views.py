from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def sign_up_page2(request):
    return render(request, 'sign_up_page2.html')

def profile_edit_page(request):
    return render(request, 'profile_edit.html')

def all_blog_page(request):
    return render(request, 'all_blog_page.html')
