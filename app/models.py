from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=200,
    )

    desc = models.TextField(
        verbose_name="Описание",
        max_length=600,
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=0,
    )

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="products/",
    )

    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        "Brand",
        verbose_name="Бренд",
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name="Товар"
        verbose_name_plural = "Товары"
    def __str__(self):
        return self.name      



class Category(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )

    parent = models.ForeignKey(
        "self",
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
        
    class Meta:
        verbose_name="Категория"
        verbose_name_plural = "Категория"
    def __str__(self):
        return self.name      


class Brand(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    site_url = models.URLField(
        verbose_name="Ссылка на сайт",
        max_length=200,
    )

    country = models.CharField(
        verbose_name="Страна",
        max_length=200,
    )
    class Meta:
        verbose_name="Бренд"
        verbose_name_plural = "Бренд"
    def __str__(self):
        return self.name    
    
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        max_length=20,
        blank=True,
        null=True,
    )
    address = models.TextField(
        verbose_name="Адрес",
        max_length=300,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username