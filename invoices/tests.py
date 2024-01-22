from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail
from django.utils import timezone
from decimal import Decimal

class InvoiceAPITests(APITestCase):

    def setUp(self):
        # Create an invoice object to be used by the test methods
        self.invoice = Invoice.objects.create(date=timezone.now(), customer_name='John Doe')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Item',
            quantity=1,
            unit_price=Decimal('100.00'),
            price=Decimal('100.00')
        )

        # URL for invoices
        self.invoice_list_url = reverse('invoice-list')
        self.invoice_detail_url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})

    def test_create_invoice(self):
        """
        Ensure we can create a new invoice object.
        """
        data = {
            'date': '2024-01-01',
            'customer_name': 'Alice Smith',
            'details': [
                {
                    'description': 'Service',
                    'quantity': 2,
                    'unit_price': '200.00',
                    'price': '400.00'
                }
            ]
        }
        response = self.client.post(self.invoice_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        self.assertEqual(Invoice.objects.get(pk=2).customer_name, 'Alice Smith')

    def test_get_invoices(self):
        """
        Ensure we can retrieve a list of invoices.
        """
        response = self.client.get(self.invoice_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_detail(self):
        """
        Ensure we can retrieve a single invoice detail by id.
        """
        response = self.client.get(self.invoice_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        """
        Ensure we can update an existing invoice.
        """
        data = {
            'date': '2024-01-02',
            'customer_name': 'Bob Brown',
            'details': [
                {
                    'id': self.invoice_detail.id,
                    'description': 'Updated Item',
                    'quantity': 3,
                    'unit_price': '150.00',
                    'price': '450.00'
                }
            ]
        }
        response = self.client.put(self.invoice_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Invoice.objects.get(pk=self.invoice.pk).customer_name, 'Bob Brown')
        self.assertEqual(InvoiceDetail.objects.get(pk=self.invoice_detail.pk).description, 'Updated Item')

    def test_partial_update_invoice(self):
        """
        Ensure we can partially update an invoice.
        """
        data = {'customer_name': 'Charlie Davis'}
        response = self.client.patch(self.invoice_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Invoice.objects.get(pk=self.invoice.pk).customer_name, 'Charlie Davis')

    def test_delete_invoice(self):
        """
        Ensure we can delete an invoice.
        """
        response = self.client.delete(self.invoice_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice.objects.filter(pk=self.invoice.pk).exists())
