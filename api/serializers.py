from rest_framework import serializers
from .models import Product, Order, OrderItem, User


# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'first_name',
#             'last_name'
#         )
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
    

class orderItemSerializer(serializers.ModelSerializer):
    # product = productSerializer(read_only=True)
    product_name = serializers.CharField(source='product.name' , read_only=True)
    product_price = serializers.DecimalField(source='product.price' , read_only=True , max_digits=10, decimal_places=2)
    class Meta:
        model = OrderItem
        fields = (
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        )
class orderSerializer(serializers.ModelSerializer):
    items = orderItemSerializer(many=True , read_only=True)
    # user = userSerializer(read_only=True) ==> to get full user data as well , if commented it will give just primary key as output (also a user serialize must be created to get full user data) 
    
    total_price = serializers.SerializerMethodField(method_name='total')
    def total(self , obj):
        order_items = obj.items.all()
        return sum([item.item_subtotal for item in order_items])
    
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'created_at',
            'status',
            'items',
            'total_price'
        )


class ProductInfoSerializer(serializers.Serializer):
    products = productSerializer(many=True , read_only=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()