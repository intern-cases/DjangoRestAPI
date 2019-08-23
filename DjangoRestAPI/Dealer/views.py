from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import DealerSerializer, DealerUpdateSerializer
from .models import Dealer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from DjangoRestAPI.accounts.api.decorators import company_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from DjangoRestAPI.accounts.api.permissions import IsOwner

# Create your views here.


@method_decorator([login_required], name='dispatch')
class DealerListAPIView(ListAPIView):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer


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
