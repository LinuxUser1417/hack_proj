from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя товара')
    price = models.FloatField(max_length=255, verbose_name='Цена товара')
    image_url = models.CharField(max_length=2083)
    rating = models.FloatField(max_length=255, verbose_name='Рекомендация товара')
    description = models.TextField(max_length=255, verbose_name='Описание товара')
    data_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    reviews_image = models.CharField(max_length=2083, default='Не указано')
    category = models.ManyToManyField(Category, max_length=255, verbose_name='Категория товара', default='Не указано')

    def __str__(self):
        return self.name
    

