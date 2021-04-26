from rest_framework import serializers

from .models import Category, Product, Mark

class ProductSerializers(serializers.ModelSerializer):
    mark_name = serializers.CharField(source='mark.get_image',read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'mark_name',
            'get_absolute_url',
            'description',
            'price',
            'ram',
            'cpu',
            'screen_size',
            'color',
            'get_image',
            'get_thumbnail'
        )

class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Category
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'products',
        )

class MarkSerializers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Mark
        fields = (
            'id', 
            'name',
            'get_image',
            'get_absolute_url',
            'products',
        )