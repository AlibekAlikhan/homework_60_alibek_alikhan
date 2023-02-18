from django.db import models


# Create your models here.



class Article(models.Model):
    status = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    price = models.DecimalField(max_digits=15, decimal_places=0, default=0, verbose_name="Цена")
    image_url = models.TextField(max_length=3000, null=True, verbose_name="Фото")
    create_at = models.DateField(verbose_name="Дата добавления")



    def str(self):
        return f"{self.status} - {self.text}"

    class Category(models.Model):
        article = models.ForeignKey(
            to='webapp.Article',
            verbose_name='Продукты',
            null=False,
            blank=False,
            related_name='categories',
            on_delete=models.RESTRICT
        )
        status_category = models.CharField(max_length=10, null=False, verbose_name="Статус")
        text_category = models.TextField(max_length=3000, null=True, verbose_name="Текст")

        def str(self):
            return f"{self.status_category} - {self.text_category}"
