"""from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView,  CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductUpdateSerializer
from .models import Product
#from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(draft=False)
        return queryset


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    #permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)"""


