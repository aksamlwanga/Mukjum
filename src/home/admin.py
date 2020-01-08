from django.contrib import admin

from  .models import Product,Images

class ProductImagesInline(admin.StackedInline):
    model = Images

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','title' ,'price','featured']
    list_filter = ['details', 'catergory']
    list_editable = ['price','featured']
    inlines = [ProductImagesInline]
    
admin.site.register(Product,ProductAdmin)