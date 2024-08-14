from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Cart model.

    Displays the list of carts with specific fields in the admin panel.
    Allows filtering carts based on user and creation date.

    List Display:
        __str__ (str): The string representation of the cart, typically showing the user's username.
        created_at (datetime): The date and time when the cart was created.
        get_total_price (float): The total price of all items in the cart, calculated dynamically.

    List Filter:
        user: Filter the list of carts by the user to whom the cart belongs.
        created_at: Filter the list of carts by their creation date.
    """

    list_display = ["__str__", "created_at", "get_total_price"]
    list_filter = ["user", "created_at"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the CartItem model.

    Displays the list of cart items with specific fields in the admin panel.
    Allows filtering of cart items based on the associated cart.

    List Display:
        cart (Cart): The cart to which the item belongs.
        product (Product): The product associated with the cart item.
        quantity (int): The number of units of the product in the cart.
        get_total_price (float): The total price of the cart item, calculated dynamically.

    List Filter:
        cart: Filter the list of cart items by the cart to which they belong.
    """

    list_display = ["cart", "product", "quantity", "get_total_price"]
    list_filter = ["cart"]
