from .views import ProductCreateAPIView,ProductDetailAPIView, ProductDeleteAPIView,\
    ProductListAPIView, ProductUpdateAPIView
from django.urls import path, include

app_name = "Product"

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list'),
    path('detail/<pk>', ProductDetailAPIView.as_view()),
    path('delete/<pk>', ProductDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', ProductUpdateAPIView.as_view(), name='update'),
    path('create/', ProductCreateAPIView.as_view(), name='create')
]
