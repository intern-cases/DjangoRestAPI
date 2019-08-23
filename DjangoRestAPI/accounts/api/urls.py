from django.urls import path, include
from DjangoRestAPI.accounts.api.views import registration_view

app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('', include('rest_auth.urls')),
]
