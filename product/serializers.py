from rest_framework.serializers import ModelSerializer

from product.models import Category, Product, Variation, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_link', 'description', 'created_date', 'category']


class VariationSerializer(ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductDetailSerializer(ProductSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = ProductSerializer.Meta.model
        fields = ProductSerializer.Meta.fields + ['description', 'tags']
