from django.contrib import admin

from .models import About, Category, Product


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.get_fields()]
    list_editable = [
        field.name for field in About._meta.get_fields() if field.name != 'id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]
    list_editable = [
        field.name for field in Product._meta.get_fields() if field.name != 'id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', "cat_name", "cat_image", )
