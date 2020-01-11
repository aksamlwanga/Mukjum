from django.contrib import admin

from  .models import Product,Images,ProductCategory,ProductSubCategory

class ProductImagesInline(admin.StackedInline):
    model = Images

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','categoryId','subCategoryId' ,'price','featured']
    list_filter = ['details', 'categoryId']
    list_editable = ['price','featured']
    inlines = [ProductImagesInline]
    
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)