from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# dynamic urls
# from django.urls import reverse

class ProductCategory(models.Model):
    categoryName                =  models.CharField(max_length=100,default="clothes")
    categoryDescription         =  models.CharField(max_length=100 ,default="shirt")
    def __str__(self):
        return 'ProductCategory:{}'.format(self.categoryName)
    def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
        return reverse("category",kwargs={"category_id":self.id})

    
class ProductSubCategory(models.Model):
    productCategoryId       =  models.ForeignKey(ProductCategory, default=None, related_name='productCategory',on_delete=models.CASCADE)
    subCategoryName         =  models.CharField(max_length=100 ,default="shirt")
    slung                   =  models.CharField(max_length=100,default="maduka")
    def __str__(self):
        return 'subcatergory:{}'.format(self.subCategoryName)
    def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
        return reverse("subcategory",kwargs={"subcategory_id":self.id})

class Product(models.Model):
    categoryId       =  models.ForeignKey(ProductCategory, default=None, related_name='category',on_delete=models.CASCADE)
    subCategoryId    =  models.ForeignKey(ProductSubCategory, default=None, related_name='subCategory',on_delete=models.CASCADE)
    name             =  models.CharField(max_length=100 ,default="shirt")
    description      =  models.TextField(blank=True,null=True)
    price            =  models.DecimalField(decimal_places=2,max_digits=10000)
    details          =  models.TextField(blank=True,null=True)
    rating           =  models.IntegerField(max_length=100000,default=1)
    featured         =  models.BooleanField(default=False)
    created          =  models.DateTimeField(auto_now_add=True)
    updated          =  models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
        return reverse("product",kwargs={"product_id":self.id})
    #  class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)
    def __str__(self):
        return 'Product:{}'.format(self.name)
    def first_image(self):
        # code to determine which image to show. The First in this case.
        return self.image[0]

class Images (models.Model):
    product = models.ForeignKey(Product, default=None, related_name='image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/products', blank=True)
    # image_thumbnail  =  ImageSpecField(source='image',
    #                                 processors=[ResizeToFill(254,363)],
    #                                 format='JPEG',
    #                                 options={'quality':60})



    