from rest_framework import serializers

from .models import Invoice, Item

# This serializer is before InvoiceSerializer because we want to use items in Invoice
class ItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Item
        read_only_fields = (
            "invoice",
        )
        fields = (
            "id",
            "title",
            "quantity",
            "unit_price",
            "net_amount",
            "vat_rate",
            "discount",
        )

class InvoiceSerializer(serializers.ModelSerializer):  

    items = ItemSerializer(many=True)
    # this field is not required to be filled out from frontend
    bankaccount = serializers.CharField(required=False)

    # this line will help us fetch name of client in Invoices.vue using invoice.client, if we do not add 
    # this line we will get 1
    # client = serializers.StringRelatedField() 

    # This is so that we can get invoice.client.name and other fields in invoice.vue
    # client = serializers.HyperlinkedRelatedField(view_name='client-detail', read_only=True)

    class Meta:
        model = Invoice
        read_only_fields = (
            "team",
            "invoice_number",
            "created_at",
            "created_by",
            "modified_at",
            "modified_by",
        ),
        fields = (
            "id",
            "invoice_number",
            "client",
            "client_name",
            "client_email",
            "client_org_number",
            "client_address1",
            "client_address2",
            "client_zipcode",
            "client_place",
            "client_country",
            "client_contact_person",
            "client_contact_reference",
            "sender_reference",
            "invoice_type",
            "due_days",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "discount_amount",
            "items",
            "bankaccount",
        )
    
    def create(self, validated_data):
        # validated-data is form data, AddInvoice.vue, post method, '/api/v1/invoices/'
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item in items_data:
            Item.objects.create(invoice=invoice, **item)
        
        return invoice
