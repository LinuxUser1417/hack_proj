from django.contrib import admin
from .models import Product, ProductImage, ProductVideo, Types, Review, ReviewImage, Favorite
# Register your models here.
admin.site.register([Product, ProductImage, ProductVideo, Types, Review, ReviewImage, Favorite])