from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# dynamic urls
# from django.urls import reverse

class Product(models.Model):
    title            =  models.CharField(max_length=100)
    catergory        =  models.CharField(max_length=100,default="clothes")
    name             =  models.CharField(max_length=100 ,default="shirt")
    description      =  models.TextField(blank=True,null=True)
    price            =  models.DecimalField(decimal_places=2,max_digits=10000)
    details          =  models.TextField(blank=True,null=True)
    featured         =  models.BooleanField(default=False)


    def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
        return reverse("product",kwargs={"product_id":self.id})
    #  class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)
    # def __str__(self):
    #     return self.name
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

    