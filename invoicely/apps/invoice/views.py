from rest_framework import viewsets
from .serializers import InvoiceSerializer, ItemSerializer
from .models import Invoice, Item
from django.core.exceptions import PermissionDenied


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        # Since user has only one team, hence .first
        team = self.request.user.teams.first()
        invoice_number = team.first_invoice_number
        team.first_invoice_number = invoice_number + 1
        team.save()
        # We need to add, bankaccount=team.bankaccount separately since this will not come from frontend, seeting this up in backend
        serializer.save(created_by=self.request.user, team=team, modified_by= self.request.user, invoice_number=invoice_number, bankaccount=team.bankaccount)
    
    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')
    
        serializer.save()

# removing this since we are already getting all the items from invoice serializer
# class ItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()

#     # This is to get all the items based on invoice id
#     def get_queryset(self):
#         # We are trying to get invoice_id from url 
#         invoice_id = self.request.GET.get('invoice_id', 0)
#         return self.queryset.filter(invoice__id=invoice_id)
    
    