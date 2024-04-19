from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from logistics.models import Category, Company, Contract
from logistics.serializers import CategorySerializer, CompanySerializer, CompanyContractSerializer, \
    ContractListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ContractListAPIView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer


class CompanyContractRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyContractSerializer
