from rest_framework import serializers

from DjangoRestAPI.accounts.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'is_company', 'is_dealer', 'is_customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['password'],
            is_company=self.validated_data['is_company'],
            is_dealer=self.validated_data['is_dealer'],
            is_customer=self.validated_data['is_customer']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            return serializers.ValidationError({'Password must match!'})

        user.set_password(password)
        user.save()
        return user

