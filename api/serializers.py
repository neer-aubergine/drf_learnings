from rest_framework import serializers
from .models import Product, Order, OrderItem

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # create a tuple if you want specific fields to be serialized
        # fields = (
        #     'id',
        #     'name',
        #     'price',
        #     'description',
        #     'stock'
        # )
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be a positive number')
        return value