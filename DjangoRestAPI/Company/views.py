from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import CompanyUpdateSerializer, CompanySerializer
from .models import Company
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from DjangoRestAPI.accounts.api.decorators import company_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from DjangoRestAPI.accounts.api.permissions import IsOwner


@method_decorator([login_required, company_required], name='dispatch')
class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer


@method_decorator([login_required, company_required], name='dispatch')
class CompanyDetailAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class CompanyDeleteAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@permission_classes([IsAdminUser | IsOwner])
@method_decorator(login_required, name='dispatch')
class CompanyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("company_name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


@permission_classes([IsAdminUser])
@method_decorator(login_required, name='dispatch')
class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
