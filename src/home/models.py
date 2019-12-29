from django.db import models
# dynamic urls
# from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=10000)
    image       =models.ImageField(null=False,blank=True,upload_to="img/products")
    featured    = models.BooleanField(default=False)


    # def get_absolute_url(self):
    #     # return f"../products/{self.id}/"
    #     return reverse("product-view",kwargs={"my_id":self.id})
    