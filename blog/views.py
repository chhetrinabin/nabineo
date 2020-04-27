from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def services(request):
    context = {}
    return render(request, 'blog/services.html', context)

def portfolio(request):
    context = {}
    return render(request, 'blog/portfolio.html', context)

def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)

def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)

def privacy(request):
    context = {}
    return render(request, 'blog/privacy.html', context)

def terms(request):
    context = {}
    return render(request, 'blog/terms-and-conditions.html', context)

