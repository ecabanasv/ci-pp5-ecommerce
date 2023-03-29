from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""
    return render(request, "home/index.html")


def about_us(request):
    """A view to return the about us page"""
    return render(request, "about_us/about_us.html")


def faq(request):
    """A view to return the faq page"""
    return render(request, "faqs/faqs.html")
