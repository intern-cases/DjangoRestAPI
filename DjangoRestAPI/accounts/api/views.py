from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer, CustomerSerializer
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from DjangoRestAPI.accounts.models import Customer
from DjangoRestAPI.accounts.api.decorators import customer_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAdminUser
from DjangoRestAPI.accounts.api.permissions import IsOwner
from rest_framework.decorators import permission_classes
from django.contrib.auth.decorators import login_required


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['email'] = user.email
            data['username'] = user.username
            data['is_company'] = user.is_company
            data['is_dealer'] = user.is_dealer
            data['is_customer'] = user.is_customer
        else:
            data = serializer.errors
        return Response(data)


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class CustomerDetailView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@permission_classes([IsAdminUser])
@method_decorator([login_required, customer_required], name='dispatch')
class CustomerCreateAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

