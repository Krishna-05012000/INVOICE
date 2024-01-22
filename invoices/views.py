from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from django.shortcuts import render
from .models import Invoice

# def invoice_list(request):
#     invoices = Invoice.objects.all()
#     return render(request, 'invoices/invoice_list.html', {'invoices': invoices})


# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer

# views.py

from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer


