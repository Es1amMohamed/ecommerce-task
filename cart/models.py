from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import ProductModel


class Cart(models.Model):
    """
    Represents a shopping cart for a user.

    Attributes:
        user (User): A one-to-one relationship with the User model, ensuring each user has a unique cart.
        created_at (datetime): The date and time when the cart was created.
        slug (str): A URL-friendly version of the user's username, generated automatically.

    Methods:
        get_total_price(): Calculates and returns the total price of all items in the cart.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f" {self.user.username}'s cart "

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a slug from the user's username.
        """

        self.slug = slugify(self.user.username)
        super(Cart, self).save(*args, **kwargs)

    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            float: The sum of the total prices of all items in the cart.
        """

        return sum(item.get_total_price() for item in self.items.all())

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ["-created_at"]


class CartItem(models.Model):
    """
    Represents an item in a shopping cart.

    Attributes:
        cart (Cart): A foreign key relationship to the Cart model, linking the item to a specific cart.
        product (ProductModel): A foreign key relationship to the Product model, linking the item to a specific product.
        quantity (int): The number of units of the product in the cart.

    Methods:
        get_total_price(): Calculates and returns the total price for the cart item.
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_price(self):
        """
        Calculate the total price for the cart item based on its quantity and unit price.

        Returns:
            float: The total price for the cart item.
        """

        return self.quantity * self.product.price

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        ordering = ["quantity"]


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    """
    Signal receiver to automatically create a cart for a new user upon user creation.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the User model that was saved.
        created (bool): A boolean indicating whether a new record was created.
    """

    if created:
        Cart.objects.create(user=instance)
