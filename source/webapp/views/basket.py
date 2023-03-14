from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DeleteView

from webapp.models import Article, Basket

from webapp.forms import OderForm

from webapp.models import Products



class BasketAddView(View):
    def post(self, request, **kwargs):
        product = get_object_or_404(Article, pk=kwargs.get('pk'))
        baskets = Basket.objects.filter(product=product.pk)
        if baskets:
            for basket in baskets:
                basket.plus()
            product.minus()
            return redirect('index_article')
        else:
            Basket.objects.create(
                product=product,
                quantity=1
            )
            product.minus()
        return redirect('index_article')


class BasketView(TemplateView):
    template_name = "basket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        basket = Basket.objects.exclude(quantity=0)
        for i in basket:
            i.sum = i.quantity * i.product.price
        context['basket'] = basket
        context['form'] = OderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OderForm(data=request.POST)
        products = Basket.objects.all()
        if form.is_valid():
            order_pk = form.save()
            for po in products:
                Products.objects.create(product_id=po.product, order_id=order_pk, count=po.quantity)
                po.delete()
            return redirect('index_article')
        return render(request, 'basket.html', context={'form': form})


class BasketDeleteView(DeleteView):
    model = Basket
    success_url = reverse_lazy('baskets_view')

