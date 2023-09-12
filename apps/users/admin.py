from django.contrib import admin
from .models import User, Shop, Category

admin.site.register([User, Category, Shop])

