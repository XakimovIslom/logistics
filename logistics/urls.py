from django.urls import path

from logistics import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('company/', views.CompanyListAPIView.as_view()),
    path('contract/', views.ContractListAPIView.as_view()),
    path('company/<int:pk>/', views.CompanyContractRetrieveAPIView.as_view()),
]
