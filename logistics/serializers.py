from rest_framework import serializers

from logistics.models import Category, Company, Contract


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("title",)


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("title", "cost", "contract_number", "auto_number", "created_at")


class CompanyContractSerializer(serializers.ModelSerializer):
    contracts = ContractSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ("contracts",)


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "title", "company", "akt", "invoice", "zayavka", "cmr", "contract_number", "cost", "auto_number",
            "created_at")
