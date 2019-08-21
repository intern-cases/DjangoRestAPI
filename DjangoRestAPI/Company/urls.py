from .views import CompanyUpdateAPIView,CompanyDetailAPIView, CompanyListAPIView,\
    CompanyCreateAPIView, CompanyDeleteAPIView
from django.urls import path, include

app_name = "Company"

urlpatterns = [
    path('', CompanyListAPIView.as_view(), name='list'),
    path('detail/<pk>', CompanyDetailAPIView.as_view()),
    path('delete/<pk>', CompanyDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', CompanyUpdateAPIView.as_view(), name='update'),
    path('create/', CompanyCreateAPIView.as_view(), name='create')
]