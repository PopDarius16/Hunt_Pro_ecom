from .views import CartItem


def cart(request):
    return {'cart': CartItem(request)}