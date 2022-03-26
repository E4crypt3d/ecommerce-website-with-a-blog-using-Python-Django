from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length=30, default="")
    sub_category = models.CharField(max_length=30, default="")
    description = models.TextField(max_length=1200, default="")
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="buybest/images/%m/%Y", default="")
    date = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Order(models.Model):
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField()

    def __str__(self):
        return self.item_json


class UpdateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        idstr = str(self.order_id)
        return idstr
