from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=1000)
  qty = models.IntegerField()
  image_url = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
    
class Cart(models.Model):
  products = models.ManyToManyField(Product)
  created_on = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
  po_number = models.CharField(max_length=12)
  
