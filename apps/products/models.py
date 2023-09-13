from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.users.models import Shop

class Types(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


# class Sticker(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='stickers/')

#     def __str__(self):
#         return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Types, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # installment_plan = models.BooleanField(default=False)
    # delivery = models.BooleanField(default=False)
    # discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # stickers = models.ManyToManyField(Sticker, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.product.name + ' Image'


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='products/videos/')

    def __str__(self):
        return self.product.name + ' Video'


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Review by {self.user} on {self.product.name}'


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/images/')

    def __str__(self):
        return self.review.product.name + ' Review Image'
