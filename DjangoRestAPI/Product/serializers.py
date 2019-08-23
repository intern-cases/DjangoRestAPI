from rest_framework import serializers
from DjangoRestAPI.Product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'dealer',
            'photo',
            'price',
            'declaration',
            'created_date',
            'modified_date',
        )



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
