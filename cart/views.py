from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from store.models import Product
from .models import CartItem


def add_to_cart(request, product_id):
    cart_item = CartItem.objects.filter(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        CartItem.objects.create(product_id=product_id)
        messages.success(request, "Item added to your cart.")
    return redirect('cart_detail')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect("cart/cart_detail")


def cart_detail(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "cart/cart_detail.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        messages.success(request, f"{product.name} added to your cart.")
        return redirect("cart/add_to_cart", product_id=product.id)

    context = {
        "product": product,
    }

    return render(request, "cart/cart_detail.html", context)

# def cart_summary(request):
#     cart = CartItem(request)
#     cart_products = cart.get_prods
#     quantities = cart.get_quants
#     totals = cart.cart_total()
#     return render(request, "cart/cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})
#
#
# def cart_add(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         product_qty = int(request.POST.get('product_qty'))
#         product = get_object_or_404(Product, id=product_id)
#         cart.add(product=product, quantity=product_qty)
#         cart_quantity = cart.__len__()
#         response = JsonResponse({'qty': cart_quantity})
#         return response
#
#
# def cart_delete(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         cart.delete(product=product_id)
#         response = JsonResponse({'product': product_id})
#         return response



