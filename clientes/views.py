import pandas as pd

from io import BytesIO
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Client, Purchase, DocumentType
from .serializers import ClientSerializer, PurchaseSerializer, DocumentTypeSerializer
from decimal import Decimal, InvalidOperation


def get_client(request):
    return render(request, 'clientes/buscar_cliente.html')


def export_client(request, cliente_id):

    try:
        cliente = Client.objects.get(id=cliente_id)
    except ObjectDoesNotExist:
        return HttpResponse("Cliente no encontrado", status=404)

    compras = Purchase.objects.filter(customer=cliente)

    data = {
        'Nombre': [cliente.first_name],
        'Apellido': [cliente.last_name],
        'Correo': [cliente.email],
        'Teléfono': [cliente.phone],
        'Total Compras': [sum(compra.amount for compra in compras)],
    }

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=cliente_{cliente_id}.xlsx'
    return response


def safe_decimal(value):
    try:
        return Decimal(str(value))  # Convertir a string antes de Decimal
    except (InvalidOperation, ValueError, TypeError):
        return Decimal("0")  # Retornar 0 si el valor es inválido

def loyalty_report(request):
    clients = Client.objects.all()

    data = []
    for client in clients:
        total_purchase = Decimal("0")
        purchase_list = Purchase.objects.filter(customer_id=client.id)
        for purchase in purchase_list:
            total_purchase += Decimal(str(purchase.amount))

        if total_purchase > Decimal("5000000"):
            data.append({
                'Nombre': client.first_name,
                'Apellido': client.last_name,
                'Correo': client.email,
                'Teléfono': client.phone,
                'Total Compras': total_purchase,
            })

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=reporte_fidelizacion.xlsx'
    return response


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        document_number = self.request.query_params.get('document_number', None)

        if document_number:
            queryset = queryset.filter(document_number=document_number)

        return queryset


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

