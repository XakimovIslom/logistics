from django.urls import path

from logistics import views

urlpatterns = [

    path('category/', views.CategoryListAPIView.as_view()),
    path('company/', views.CompanyListAPIView.as_view()),

    path('company/<int:pk>/contracts/', views.CompanyContractListAPIView.as_view()),
    path('company/<int:company_pk>/contracts/<int:contract_pk>/', views.CompanyContractRetrieveAPIView.as_view()),
]
