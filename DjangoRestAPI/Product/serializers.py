from rest_framework import serializers
from DjangoRestAPI.Product.models import Product, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'product',
            'is_active',
            'discount_price',
            'discount_finish',
        )


class ProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(many=True, read_only=True)

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
            'discount',
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

