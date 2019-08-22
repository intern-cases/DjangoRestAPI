from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .serializers import DealerSerializer, DealerUpdateSerializer
from .models import Dealer
# Create your views here.


class DealerListAPIView(ListAPIView):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer


class DealerDetailAPIView(RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerDeleteAPIView(DestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


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


class DealerCreateAPIView(CreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerUpdateSerializer

