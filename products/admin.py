from django.contrib import admin
from .models import Category, Product

# Register your models here.
# sur github atelier 2 readme

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','category','created_at')
    list_filter = ('category',)
    search_fields = ('name','description')