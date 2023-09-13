from rest_framework import serializers
from .models import Types, Product, ProductImage, ProductVideo, Review, ReviewImage

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = '__all__'

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    videos = ProductVideoSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('shop', 'rating')

    def create(self, validated_data):
        user = self.context.get('user')
        shop = user.shop
        product = Product.objects.create(shop=shop, **validated_data)
        return product
