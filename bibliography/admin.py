# -*- coding: utf-8 -*-
from models import Book, BookCategory
from django.contrib import admin
from django.db.models.aggregates import Count


class BookAdmin(admin.ModelAdmin):
    list_display = ('author_as_text', 'title', 'publication_as_text',
                    'category', 'discipline')
    list_filter = ['category', 'discipline', ]


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_book_count']
    ordering = ['-book__count', ]

    def queryset(self, request):
        return super(BookCategoryAdmin, self)\
            .queryset(request)\
            .annotate(Count('book'))

    def show_book_count(self, instance):
        return instance.book__count
    show_book_count.admin_order_field = 'book__count'
    show_book_count.short_description = u'מספר ספרים'

admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)
