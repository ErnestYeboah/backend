from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["productName", "price", "category"]
    search_fields = ['productName', 'category']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["productName", "price", "date_added"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["productName", "price", "category", "date_added"]