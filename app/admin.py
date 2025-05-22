from django.contrib import admin
from .models import Product, Category, Brand, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass