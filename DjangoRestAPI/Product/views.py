from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView,  CreateAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductUpdateSerializer
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from DjangoRestAPI.accounts.api.permissions import IsOwner
from DjangoRestAPI.accounts.api.decorators import dealer_required
from DjangoRestAPI.accounts.models import Customer
from DjangoRestAPI.Dealer.models import Dealer
# Create your views here.


@method_decorator(login_required, name='dispatch')
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


@method_decorator(login_required, name='dispatch')
class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
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


@method_decorator([login_required, dealer_required], name='dispatch')
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
