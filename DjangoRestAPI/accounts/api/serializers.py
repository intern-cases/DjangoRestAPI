from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from DjangoRestAPI.accounts.models import User, Customer


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'is_company', 'is_dealer', 'is_customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User.objects.create(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=make_password(self.validated_data['password']),
            is_company=self.validated_data['is_company'],
            is_dealer=self.validated_data['is_dealer'],
            is_customer=self.validated_data['is_customer']
        )
        password2 = self.validated_data['password2']
        if user.password != password2:
            return serializers.ValidationError({'Password must match!'})

        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['location', 'is_active']
