from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# dynamic urls
# from django.urls import reverse

class Product(models.Model):
    title            =  models.CharField(max_length=100)
    catergory        =  models.CharField(max_length=100 ,default="clothes")
    name             =  models.CharField(max_length=100 ,default="shirt")
    description      =  models.TextField(blank=True,null=True)
    price            =  models.DecimalField(decimal_places=2,max_digits=10000)
    image            =  models.ImageField(null=False,blank=True,upload_to="img/products")
    image_thumbnail  =  ImageSpecField(source='image',
                                    processors=[ResizeToFill(254,363)],
                                    format='JPEG',
                                    options={'quality':60})
    details          =  models.TextField(blank=True,null=True)
    featured         =  models.BooleanField(default=False)


    # def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
    #     return reverse("product-view",kwargs={"my_id":self.id})
    