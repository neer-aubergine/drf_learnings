from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.serializers import productSerializer , orderSerializer , orderItemSerializer
from api.models import Product , Order , OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    # if using JsonResponse , use this : 
    # return JsonResponse({
    #         "data" : serializer.data
    # })

    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request , pk):
    products = get_object_or_404(Product , pk=pk)
    serializer = productSerializer(products)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)