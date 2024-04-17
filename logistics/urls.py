from django.urls import path

from logistics import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('company/', views.CompanyListView.as_view()),
    path('contract/', views.ContractListView.as_view()),
]
