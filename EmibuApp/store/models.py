from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=128, default="zivotinje")
    name = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class OrderProduct(models.Model):
    type = models.CharField(max_length=128, default="zivotinje")
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cart(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through='CartLine')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customerID.first_name} {self.customerID.last_name} - {self.total_price} - {self.order_date}"

class CartLine(models.Model):
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(OrderProduct, through='OrderLine', related_name='order_products')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=128, default="Trg Bana Josipa Jelacica 10, 10000 Zagreb, Croatia")
    first_name = models.CharField(max_length=128, default="")
    last_name = models.CharField(max_length=128, default="")
    email = models.CharField(max_length=64, default="")
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        if self.customerID is None:
            return f"{self.id} Anonymous - {self.products.all()} - {self.order_date}"
        return f"{self.id} {self.customerID.first_name} {self.customerID.last_name} - {self.products.all()} - {self.order_date}"
    
class OrderLine(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
class CustomProject(models.Model):
    title = models.CharField(max_length=128, default="No title")
    request_text = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title