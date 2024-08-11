from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from .models import ProductModel
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for handling CRUD operations on Product models.

    This ViewSet provides endpoints to perform create, read, update, and delete
    operations on `ProductModel` instances, and supports ordering and searching.

    Attributes:
    - queryset: The set of `ProductModel` instances that this ViewSet will operate on.
    - serializer_class: The serializer class used to serialize and deserialize `ProductModel` instances.
    - filter_backends: List of filter backends used for filtering and searching results.
    - ordering_fields: List of fields that can be used for ordering the query results.
    - ordering: Default ordering of query results by the specified fields.
    - search_fields: List of fields that can be searched using the search filter.

    Methods:
    - list: Retrieve a list of products, optionally ordered and filtered based on query parameters.
    - create: Create a new product instance.
    - retrieve: Retrieve a specific product instance by its primary key.
    - update: Update an existing product instance.
    - partial_update: Partially update an existing product instance.
    - destroy: Delete a specific product instance.
    """

    queryset = ProductModel.objects.all().order_by("price")
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["price"]
    ordering = ["price"]
    search_fields = ["name"]
