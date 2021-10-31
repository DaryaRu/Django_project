from shop.models.cart_item import CartItem
from rest_framework import mixins, status, viewsets
from shop.serializers.cart_item_serializer import CartItemSerializer
from rest_framework.response import Response

class CartItemViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.get_queryset().filter(created_by=request.user.id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by = request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        