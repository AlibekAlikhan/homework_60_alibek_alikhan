from django.db import models
from django.db.models import TextChoices


# Create your models here.

class StatusChoice(TextChoices):
    OTHER = 'other', 'разное'
    TECHNIQUE = 'technique', 'техника'
    CLOTH = 'cloth', 'одежда'
    TOYS = 'toys', 'игрушки'


class Article(models.Model):
    category = models.CharField(verbose_name="Категория", choices=StatusChoice.choices, max_length=20,
                                default=StatusChoice.OTHER)
    name = models.CharField(max_length=100, null=False, verbose_name="Имя")
    text = models.TextField(max_length=2000, null=True, verbose_name="Текст")
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="Цена")
    remainder = models.IntegerField(verbose_name="Остаток")
    image_url = models.TextField(max_length=3000, null=True, verbose_name="Фото")
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    def str(self):
        return f"{self.name} - {self.price}"
