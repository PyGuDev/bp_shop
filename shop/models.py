from django.db import models


class CategoryProduct(models.Model):
    """
    Модель категории товаров
    """
    title = models.CharField('Название', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class ImagesForProduct(models.Model):
    """
    Модель изображений
    """
    url = models.ImageField('Изображение', upload_to='uploads/products',  blank=True, null=True)

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Products(models.Model):
    """
    Модель товаров
    """
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Название товара', max_length=500, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)
    vk_profile = models.CharField('URL профиля Vk', max_length=400, blank=True, null=True)
    whats_app_profile = models.CharField('Номер тел. WhatsApp', max_length=12, blank=True, null=True)
    telegram_profile = models.CharField('Номер тел. WhatsApp', max_length=12, blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=12, blank=True, null=True)
    author = models.ForeignKey('user.CustomUser', verbose_name='Автор', on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(ImagesForProduct, related_name='rel_images', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

