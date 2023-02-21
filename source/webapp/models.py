from django.db import models


# Create your models here.

class Category(models.Model):
    status_category = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text_category = models.TextField(max_length=3000, null=True, verbose_name="Текст")

    def str(self):
        return f"{self.status_category} - {self.text_category}"


class Article(models.Model):
    category = models.ForeignKey(
        to='webapp.Category',
        verbose_name='категории',
        null=False,
        blank=False,
        related_name='articles',
        on_delete=models.RESTRICT
    )
    name = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    price = models.DecimalField(max_digits=15, decimal_places=0, default=0, verbose_name="Цена")
    image_url = models.TextField(max_length=3000, null=True, verbose_name="Фото")
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    def str(self):
        return f"{self.name} - {self.price}"
