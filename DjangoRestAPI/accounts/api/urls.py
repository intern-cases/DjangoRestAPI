from django.urls import path, include
from DjangoRestAPI.accounts.api.views import registration_view, CustomerDetailView, CustomerCreateAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('customer/', CustomerDetailView.as_view(), name='customer'),
    path('customer/create', CustomerCreateAPIView.as_view(), name='create'),
    path('', include('rest_auth.urls')),
]
