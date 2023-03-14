from django import forms
from django.core.exceptions import ValidationError

from webapp.models.article import Article

from webapp.models import Order


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("category", "name", "text", "price", "image_url", "remainder")
        labels = {
            'category': 'Категория',
            'name': 'Имя',
            'text': 'Текст',
            'price': 'Цена',
            'image_url': 'Фото',
            "remainder": "Остаток"
        }

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if len(text) <= 2:
            raise ValidationError("Заполните линию")
        return text

    def clean_remainder(self):
        remainder = self.cleaned_data.get("remainder")
        if remainder < 0:
            raise ValidationError("Остаток меньше 0 не должно быть")
        return remainder


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class OderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("name", "email", "phone")
        labels = {
            'name': 'Имя',
            'email': 'Email',
            'phone': 'Телефон'
        }
