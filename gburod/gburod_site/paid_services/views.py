from django.shortcuts import render
from paid_services.models import PricePdfDoc


def paid_services(request):
    template = 'paid_services/services.html'

    pdf_docs = PricePdfDoc.objects.filter(published=True)
    context = {
        'pdf_docs': pdf_docs,
    }

    return render(request, template, context)
