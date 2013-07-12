from django.views.generic.list import ListView
from backoffice.views import DisciplineMixin
from models import Book, BookCategory
from django.shortcuts import get_object_or_404


class DisciplineFilterMixin(DisciplineMixin):
    def get_queryset(self):
        return super(DisciplineFilterMixin, self)\
            .get_queryset().filter(discipline=self.discipline)


class DisciplineBooksContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(DisciplineBooksContextMixin, self)\
            .get_context_data(**kwargs)
        category_ids = Book.objects.filter(discipline=self.discipline)\
                                   .values_list('category', flat=True)\
                                   .distinct()
        context['categories'] = BookCategory.objects.filter(pk__in=category_ids)
        return context


class BookListView(DisciplineBooksContextMixin,
                   DisciplineFilterMixin, ListView):
    paginate_by = 20
    model = Book


class FilterByBookCategoryMixin(object):
    def get_queryset(self):
        self.category = get_object_or_404(BookCategory, pk=self.args[0])
        return super(FilterByBookCategoryMixin, self)\
            .get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(FilterByBookCategoryMixin, self)\
            .get_context_data(**kwargs)
        context['category'] = self.category
        return context


class BookListViewByCategory(FilterByBookCategoryMixin, BookListView):
    pass
