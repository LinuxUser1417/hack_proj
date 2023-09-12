from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(max_length=2566, verbose_name='Описание')
    category = models.CharField(max_length=255, verbose_name='Категория')
    rating = models.FloatField(verbose_name='Рейтинг')
    publication_date = models.DateField(verbose_name='Дата публикации')
    stickers = models.CharField(max_length=255, verbose_name='Стикеры')
    installment = models.BooleanField(default=False, verbose_name='Рассрочка')
    delivery = models.BooleanField(default=False, verbose_name='Доставка')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='Скидка')

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    text = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    image = models.ImageField(upload_to='reviews/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'Отзыв на товар "{self.product.name}"'

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos', verbose_name='Товар')
    image = models.ImageField(upload_to='product/photos/', verbose_name='Фотография')

class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos', verbose_name='Товар')
    video_url = models.URLField(max_length=200, verbose_name='Ссылка на видео')
