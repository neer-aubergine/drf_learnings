from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/info/', views.product_info),
    path('products/<int:pk>/', views.product_detail),
    path('orders/', views.order_list),
    # path('orders/<int:pk>/', views.order_detail),
    # path('users/', views.user_list),
    # path('users/<int:pk>/', views.user_detail),
]
