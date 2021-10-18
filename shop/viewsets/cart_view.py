from shop.models.cart import Cart
from rest_framework import mixins, status, viewsets
from shop.serializers.cart_serializer import CartSerializer
from rest_framework.response import Response

class CartViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.get_queryset().filter(created_by=request.user.id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    
