from rest_framework import serializers
from DjangoRestAPI.Product.models import Product, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            '',
            '',
            '',
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'dealer',
            'photo',
            'price',
            'is_discount',
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
            'is_discount',
            'photo',
            'is_active',
            'price',
        )

    def save(self):
        product = Product.objects.create(
            dealer=self.validated_data['dealer'],
            declaration=self.validated_data['declaration'],
            is_discount=self.validated_data['is_discount'],
            photo=self.validated_data['photo'],
            price=self.validated_data['price'],
        )

        product.save()
        return product

