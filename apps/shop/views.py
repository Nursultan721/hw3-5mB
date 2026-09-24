from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shop
from .serializers import ShopSerializer


class ShopListCreateView(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        is_active = request.query_params.get('is_active')
        if is_active is not None:
            shops = shops.filter(is_active=is_active.lower() in ('true', '1', 'yes'))
        return Response(ShopSerializer(shops, many=True).data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShopDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Shop, pk=pk)

    def get(self, request, pk):
        return Response(ShopSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)