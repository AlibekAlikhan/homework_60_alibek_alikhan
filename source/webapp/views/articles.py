from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models.article import Article

from webapp.forms import ArticleForm

from webapp.forms import SearchForm


class ArticleView(ListView):
    template_name = "tasks.html"
    model = Article
    context_object_name = "articles"
    ordering = ['-create_at']
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(category__icontains=self.search_value)
            queryset = queryset.filter(query).exclude(is_deleted=True).exclude(remainder=0)
        return queryset.exclude(is_deleted=True).exclude(remainder=0)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductCreateView(CreateView):
    template_name = "product_create.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    template_name = 'detail_article.html'
    model = Article


class ProductUpdateView(UpdateView):
    model = Article
    template_name = "product_update.html"
    form_class = ArticleForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'delete_confirm.html'
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('index_article')

    def get(self, request, *args, **kwargs):
        return self.delete(request)


