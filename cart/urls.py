from django.urls import path
from . import views


urlpatterns = [
    path('cart_detail/', views.add_to_cart, name='cart_detail'),
    path("remove/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("", views.cart_detail, name="cart_detail"),
]