from django.contrib import admin
from .models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_filter = ["price"]
    ordering = ["price"]
