from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import datetime
import os

# Create your models here.

#image name change 
def image_name_change(instance,filename):
    basename = "images"
    ext = filename.split('.')[-1]
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = ".".join([suffix,ext])
    return os.path.join(basename,filename)


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200,null=True)
    image= models.ImageField(upload_to= image_name_change, blank=False,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital= models.BooleanField(default=False,null=True, blank=False)
    image= models.ImageField(upload_to= image_name_change,blank=False,null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url= self.image.url 
        except:
            url=''
        return url


class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_chart_total(self):
        orderitems= self.orderitem_set.all()
        total =sum([item.get_total for item in orderitems]) 
        return total 

    @property
    def get_total_quantity(self):
        orderitems= self.orderitem_set.all()
        total =sum([item.quantity for item in orderitems]) 
        return total 



class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, blank= True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address= models.CharField(max_length=200, null=True)
    city= models.CharField(max_length=200, null=True)
    state= models.CharField(max_length=200, null=True)
    zipcode= models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
