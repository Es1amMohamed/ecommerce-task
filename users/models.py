from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    """
    Represents additional profile information for a user.

    This model is used to store supplementary details about a user,
    extending the built-in Django `User` model with additional fields.

    Fields:
    - user: A one-to-one relationship with the Django `User` model.
    - first_name: The first name of the user.
    - last_name: The last name of the user.
    - email: The email address of the user.
    - created_at: The date and time when the profile was created, automatically set on creation.

    Meta:
    - ordering: Orders the profiles by the `created_at` field in descending order.
    - verbose_name_plural: The plural name of the model, used in admin interfaces and other places.
    - verbose_name: The singular name of the model, used in admin interfaces and other places.

    Methods:
    - __str__: Returns the username of the associated user for display purposes.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "users"
        verbose_name = "user"

    def __str__(self):
        return self.user.username
