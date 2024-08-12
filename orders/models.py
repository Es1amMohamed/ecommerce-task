from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import ProductModel


class OrderModel(models.Model):
    ORDER_STATUS = (
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
    )

    PAYMENT_STATUS = (
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
    )

    PAYMENT_METHOD = (
        ("Cash", "Cash"),
        ("Card", "Card"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=20, default="")
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default="Processing"
    )
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS, default="Unpaid"
    )
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, default="Cash"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "orders"
        verbose_name = "order"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(OrderModel, self).save(*args, **kwargs)
