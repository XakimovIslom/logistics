from rest_framework import serializers

from logistics.models import Category, Company, Contract


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title",)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "title",)


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("id", "title", "cost", "contract_number", "auto_number", "created_at")


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "id", "title", "company", "contract_number", "cost", "auto_number",
            "created_at")


class ContractListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("id", "title", "akt", "invoice", "zayavka", "cmr")
