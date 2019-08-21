from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView,  CreateAPIView
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


"""class DealerCreateAPIView(CreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerUpdateSerializer"""

from django.contrib.auth import login
from django.views.generic import CreateView

from ..forms import DealerSignUpForm
from DjangoRestAPI.accounts.models import User


class StudentSignUpView(CreateView):
    model = User
    form_class = DealerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)