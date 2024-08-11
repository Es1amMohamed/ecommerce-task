from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to handle the serialization and deserialization
    of User instances, including validation and transformation of data.

    Fields:
    - username: The username of the user.
    - password: The password of the user. Note that passwords should be
      handled with care and are typically hashed before being stored.

    Meta:
    - model: The model associated with this serializer, which is User.
    - fields: A list of fields to be included in the serialized representation.
    """

    class Meta:
        model = User
        fields = ["username", "password"]
