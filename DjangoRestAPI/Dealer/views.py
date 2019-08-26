from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import DealerSerializer, DealerUpdateSerializer
from .models import Dealer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from DjangoRestAPI.accounts.api.permissions import IsOwner
from DjangoRestAPI.accounts.models import Customer
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point


# Create your views here.


@method_decorator([login_required], name='dispatch')
class DealerListAPIView(ListAPIView):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer

    def list(self, request):
        user = self.request.user
        if user.is_customer is True:
            customer = Customer.objects.filter(user=user)
            point_array = customer.location.split(",")
            lat = float(point_array[0])
            lng = float(point_array[1])
            point = Point(lat, lng)
            radius = 500
            queryset = Dealer.objects.filter(location_lte=(point, D(km=radius)))
            serializer = DealerSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(404)


@method_decorator([login_required], name='dispatch')
class DealerDetailAPIView(RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class DealerDeleteAPIView(DestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class DealerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class DealerCreateAPIView(CreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
