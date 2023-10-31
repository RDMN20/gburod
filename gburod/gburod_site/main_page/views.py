from django.shortcuts import render


def index(request):
    template = 'main_page/index.html'
    return render(request, template)


def about_us(request):
    template = 'main_page/about.html'
    return render(request, template)
