from rest_framework import serializers
from .models import Client, Purchase, DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer()

    class Meta:
        model = Client
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
