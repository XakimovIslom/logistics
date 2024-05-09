from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics

from logistics.models import Company, Contract, Category
from logistics.serializers import ContractListRetrieveSerializer, CategorySerializer, CompanySerializer, \
    ContractListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class CompanyContractListAPIView(generics.ListAPIView):
    serializer_class = ContractListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404("Company does not exist")
        return company.contracts.all()


class CompanyContractRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ContractListRetrieveSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        company_pk = self.kwargs.get('company_pk')
        contract_pk = self.kwargs.get('contract_pk')
        try:
            return Contract.objects.get(company_id=company_pk, pk=contract_pk)
        except Contract.DoesNotExist:
            raise Http404("Contract does not exist")
