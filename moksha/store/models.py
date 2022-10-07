from email.policy import default
from random import choices
from django.urls import reverse
from email.mime import image
from unicodedata import category
from django.db import models
from category.models import Category
from django_extensions.db.fields import AutoSlugField
# Create your models here.

class Product(models.Model):
    product_name    =models.CharField(max_length=200,unique=True)
    slug            =  AutoSlugField(populate_from='product_name', max_length=255,unique=True,null=True, blank=True,)
    description     =models.TextField(max_length=500,blank=True)
    brand           =models.CharField(max_length=200,null=True)
    price           =models.IntegerField()   
    old_price       =models.IntegerField(null=True)
    images          =models.ImageField(upload_to='photos/product_img')
    stock           =models.IntegerField()
    is_available    =models.BooleanField(default=True)
    category        =models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date    =models.DateTimeField(auto_now_add=True)
    modified_date   =models.DateTimeField(auto_now=True)



    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name 



class VariationManager(models.Manager):
    def colors(self,):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)
    
    def batteries(self):
        return super(VariationManager,self).filter(variation_category='battery',is_active=True)



variation_category_choice=(
    ('color','color'),
    ('battery','battery'),
)



class Variation(models.Model):
    product            = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100,choices=variation_category_choice)
    variation_value    =models.CharField(max_length=100)
    is_active          =models.BooleanField(default=True)
    created_date       =models.DateTimeField(auto_now=True)

    objects=VariationManager()


    def __str__(self):
        return self.variation_value




