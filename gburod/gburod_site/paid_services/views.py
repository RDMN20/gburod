from django.shortcuts import render


def paid_services(request):
    template = 'paid_services/services.html'
    return render(request, template)
