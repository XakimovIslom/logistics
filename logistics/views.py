from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from logistics.models import Category, Company, Contract
from logistics.serializers import CategorySerializer, CompanySerializer, ContractSerializer, CompanyContractSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ContractListView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class CompanyContractListView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyContractSerializer
