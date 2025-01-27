from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImage(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'