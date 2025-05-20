def index(request):
products = Product.objects.all()
context = {"products": products}
return render(request, "app/index.html", context)

admin.site.register(Product)
admin.site.register(Category)

    slug = models.SlugField(
        "URL",
        unique = True,
        null= True,
        blank=True,
        max_length = 250,
        editable=True,
    )

    class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
