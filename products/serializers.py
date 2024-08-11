from rest_framework import serializers
from .models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    """
        Serializer for the ProductModel.

        This serializer is used to convert `ProductModel` instances into JSON format
        and vice versa. It handles validation, serialization, and deserialization of
        product data.

    Meta:
    - model: The model associated with this serializer, which is `ProductModel`.
    - fields: A tuple specifying the fields to be included in the serialized representation.
    """

    class Meta:
        model = ProductModel
        fields = ("name", "price")
