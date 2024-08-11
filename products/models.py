from django.db import models
from django.utils.text import slugify


class ProductModel(models.Model):
    """
    Represents a product in the system.

    This model stores information about a product, including its name, price,
    and timestamps for creation and updates. It also generates a slug based on
    the product's name for URL-friendly representations.

    Meta:
    - ordering: Orders products by the `created_at` field in descending order (newest first).
    - verbose_name_plural: The plural name of the model, used in admin interfaces and other places.
    - verbose_name: The singular name of the model, used in admin interfaces and other places.

    Methods:
    - __str__: Returns the name of the product for display purposes.
    - save: Overrides the default save method to generate and set the `slug` field.
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "products"
        verbose_name = "product"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductModel, self).save(*args, **kwargs)
