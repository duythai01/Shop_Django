from django.shortcuts import render
from django_filters import OrderingFilter
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Category, Product, Tag
from product.paginator import BasePagination
from product.serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = BasePagination

    # queryset = Product.objects.filter(active=True)

    def get_queryset(self):
        products = Product.objects.filter(active=True)
        q = self.request.query_params.get('q')
        if q is not None:
            products = products.filter(name__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id is not None:
            products = products.filter(category_id=cate_id)

        return products

    # @action(methods=['post'], detail=True, url_path='Tags')
    # def add_tag(self, request, pk):
    #     try:
    #         product = self.get_object()
    #     except Http404:
    #         return Response(status=status.HTTP_400_NOT_FOUND)
    #     else:
    #         tags = request.data.get('tags')
    #         if tags is not None:
    #             for tag in tags:
    #                 t, _ = Tag.objects.get_or_create(name=tag)
    #                 product.tags.add(t)
    #
    #             product.save()
    #
    #             return Response(self.serializer_class(product).data,
    #                             status=status.HTTP_201_CREATED)


class ProductDetailViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductDetailSerializer

    @action(methods=['post'], detail=True, url_path='Tags')
    def add_tag(self, request, pk):
        try:
            product = self.get_object()
        except Http404:
            return Response(status=status.HTTP_400_NOT_FOUND)
        else:
            tags = request.data.get('tags')
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    product.tags.add(t)

                product.save()

                return Response(self.serializer_class(product).data,
                                status=status.HTTP_201_CREATED)


class SearchViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = ProductDetailSerializer

    # filter_backends = [SearchFilter, OrderingFilter]
    # filter_fields = ['name', 'price', 'description', 'tags']
    def get_queryset(self):
        products = Product.objects.filter(active=True)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            products = products.filter(name__icontains=keyword)
        product_id = self.request.query_params.get('id')
        if id is not None:
            products = products.filter(category_id=product_id)

        return products
