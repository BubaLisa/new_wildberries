from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

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

    slug = models.SlugField(
        "URL",
        max_length=250,
        unique=True,
        null=False,
        editable=True,
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

    slug = models.SlugField(
        "URL",
        max_length=250,
        unique=True,
        null=False,
        editable=True,
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
    















    
'''class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email'''