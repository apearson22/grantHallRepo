from django.db import models

class Client(models.Model):
    customerID = models.IntegerField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    cadet = models.BooleanField(default=False)
    faculty = models.BooleanField(default=False)
    stockPerson = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

class Order(models.Model):
    receiveDate = models.DateField()
    paid = models.BooleanField(default=False)
    orderID = models.IntegerField()
    orderType = models.CharField(max_length=30)
    foodID = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.orderID

class Item(models.Model):
    foodID = models.IntegerField()
    stockQuantity = models.IntegerField()
    foodName = models.CharField(max_length=30)
    price = models.IntegerField()
    espirationDate = models.DateField()
    calories = models.IntegerField()
    sodium = models.IntegerField()
    sugar = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (self.foodID, self.quantity, self.price)

class Delivery(models.Model):
    companyName = models.CharField(max_length=30)
    foodID = models.IntegerField()
    location = models.CharField(max_length=30)
    deliveryDate = models.DateField()
    deliveryCharge = models.IntegerField()
    deliveryQuantity =models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (self.companyName, self.foodID, self.deliveryDate)
