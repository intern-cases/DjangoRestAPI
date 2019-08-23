from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'succesfully registered user'
            data['email'] = user.email
            data['username'] = user.username
            data['is_company'] = user.is_company
            data['is_dealer'] = user.is_dealer
            data['is_customer'] = user.is_customer
        else:
            data = serializer.errors
        return Response(data)
