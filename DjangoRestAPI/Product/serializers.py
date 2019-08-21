from rest_framework import serializers
from DjangoRestAPI.Product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField()

    class Meta:
        fields = (
            'dealer',
            'photo',
            'price',
            'declaration',
            'created_date',
            'modified_date',
        )
        model = Product


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'dealer',
            'declaration',
            'photo',
            'is_active',
            'price',
        )
