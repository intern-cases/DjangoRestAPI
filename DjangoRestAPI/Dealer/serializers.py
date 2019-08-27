from rest_framework import serializers
from DjangoRestAPI.Dealer.models import Dealer
from DjangoRestAPI.Product.serializers import ProductSerializer


class DealerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Dealer
        fields = (
            'name',
            'company',
            'establish_year',
            'is_active',
            'location',
            'created_date',
            'modified_date',
            'products',
        )


class DealerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealer
        fields = (
            'name',
            'company',
            'establish_year',
            'location',
        )
