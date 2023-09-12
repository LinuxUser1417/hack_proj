from django.contrib import admin
from .models import Product, Review, Photo, Video

admin.site.register([Product, Review, Photo, Video])