from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Article


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