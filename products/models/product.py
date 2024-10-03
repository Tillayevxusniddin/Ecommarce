from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(default=0)    #omborda ushbu obyektdan nechta ekanligi


    def __str__(self):
        return self.name

    def is_in_stock(self):  # omnborda qoganmi yani 0 dan katta bolsa qolgan boladi
        return self.stock > 0

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            return False   #agar ombordan kora soralvotgan miqdor kop bolsa False

        self.stock -= quantity  #osha obyekt stockini miqdor ya'ni quantityga kamaytiramiz
        self.save()

    def increase_stock(self, amount):  #omborga narsa qoyish
        self.stock += amount
        self.save()

    class Meta:
        ordering = ['name']

