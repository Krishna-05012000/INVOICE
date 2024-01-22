from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

# router = DefaultRouter()
# router.register(r'invoices', views.InvoiceViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
router = DefaultRouter()

router.register(r'invoices', InvoiceViewSet, basename='invoice')
"""
GET /invoices/: List all invoices.
POST /invoices/: Create a new invoice.
GET /invoices/{pk}/: Retrieve a specific invoice by its primary key (pk).
PUT /invoices/{pk}/: Update a specific invoice by its primary key.
PATCH /invoices/{pk}/: Partially update a specific invoice.
DELETE /invoices/{pk}/: Delete a specific invoice.
"""
router.register(r'invoicedetails', InvoiceDetailViewSet, basename='invoicedetail')

urlpatterns = [
    path('', include(router.urls)),
]
