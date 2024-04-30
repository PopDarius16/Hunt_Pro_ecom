from django.db import models
from store.models import Product
from django.urls import reverse


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Poți adăuga și alte câmpuri, cum ar fi utilizatorul (dacă este nevoie)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")

