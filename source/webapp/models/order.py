from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(to="webapp.Article", related_name="produc", blank=True, through="Products")
    name = models.CharField(max_length=100, null=False, verbose_name="Имя")
    email = models.CharField(max_length=100, null=False, verbose_name="Email")
    phone = models.CharField(max_length=100, null=False, verbose_name="Телефон")
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")


class Products(models.Model):
    product_id = models.ForeignKey('webapp.Article', related_name='product', on_delete=models.CASCADE,
                                   verbose_name="Продукт")
    order_id = models.ForeignKey('webapp.Order', related_name='orders', on_delete=models.CASCADE,
                                 verbose_name="Заказ")
    count = models.IntegerField(verbose_name='Количество')
