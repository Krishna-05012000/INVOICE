from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()

        details = validated_data.get('details')
        if details is not None:
            for detail_data in details:
                detail_id = detail_data.get('id', None)
                if detail_id:
                    detail = InvoiceDetail.objects.get(id=detail_id, invoice=instance)
                    detail.description = detail_data.get('description', detail.description)
                    detail.quantity = detail_data.get('quantity', detail.quantity)
                    detail.unit_price = detail_data.get('unit_price', detail.unit_price)
                    detail.price = detail_data.get('price', detail.price)
                    detail.save()
                else:
                    InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance
