from rest_framework import serializers
from DjangoRestAPI.Product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField()

    class Meta:
        model = Product
        fields = {
            'dealer',
            'photo',
            'price',
            'declaration',
            'is_active',
            'created_date',
            'modified_date',
        }


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'declaration',
            'photo',
            'is_active',
        ]
