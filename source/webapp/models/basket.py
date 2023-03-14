from django.db import models



class Basket(models.Model):
    product = models.ForeignKey('webapp.Article', related_name='products', on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.IntegerField(verbose_name="Количество")

    def plus(self, using=None, keep_parents=False):
        self.quantity += 1
        self.save()

    def minus(self, using=None, keep_parents=False):
        self.quantity -= 1
        self.save()
