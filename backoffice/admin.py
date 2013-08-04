# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from imagekit.admin import AdminThumbnail
from modeltranslation.admin import TranslationAdmin
from django.db.models import Count
from form_utils.widgets import ImageWidget
import models
from django.db.models import ImageField
from django.contrib.auth.admin import UserAdmin
from moderation.admin import ModerationAdmin

TranslationAdmin.actions_on_bottom = True
TranslationAdmin.actions_on_top = False
TranslationAdmin.ordering = ('name_he',)


class TranslatedModelAdmin(TranslationAdmin):
    # search_fields = ['name_he']
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class WithWorkCountField(object):
    ordering = ['-work__count']

    def queryset(self, request):
        return super(WithWorkCountField, self)\
            .queryset(request)\
            .annotate(Count('work'))

    def show_work_count(self, instance):
        return instance.work__count
    show_work_count.admin_order_field = 'work__count'
    show_work_count.short_description = u'מספר עבודות'


class DisciplineAdmin(WithWorkCountField, TranslationAdmin):
    list_display = ('name_he', 'name_en', 'active', 'show_work_count')


class LargeImagePreviewInChangeForm(object):
    formfield_overrides = {
        ImageField: {'widget': ImageWidget()},
    }


class WorkAdmin(ModerationAdmin, LargeImagePreviewInChangeForm, TranslationAdmin):
    admin_thumbnail = AdminThumbnail(image_field='processed_image')
    admin_thumbnail.short_description = u'תצוגה מקדימה'
    list_display = ('get_raw_image_filename', 'name', 'designer',
                    'category', 'discipline', 'admin_thumbnail')
    ordering = ('-id',)
    list_filter = ('discipline', 'category', 'designer', 'of_collections')
    filter_horizontal = ['subjects', 'of_collections']
    readonly_fields = ['get_raw_image_filename', ]
    fields = ['raw_image', 'designer', 'name', 'get_raw_image_filename', 'category', 'tags',
              'discipline', 'publish_date_as_text', 'publish_year',
              'size_as_text', 'height',
              'width', 'depth', 'country', 'client', 'technique',
              'of_collections', 'is_self_collected', 'subjects', 'description',
              ]

    def get_raw_image_filename(self, instance):
        import os
        if instance.raw_image:
            return os.path.basename(instance.raw_image.name)
        return None
    get_raw_image_filename.short_description = u'שם קובץ'
    get_raw_image_filename.admin_order_field = 'raw_image'

    def queryset(self, request):
        qs = super(WorkAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(
            designer=request.user.get_profile().in_charge_of_designers.all()
        )


class DesignerAdmin(LargeImagePreviewInChangeForm, WithWorkCountField,
                    TranslationAdmin):
    list_display = (
        'name', 'main_discipline', 'generation_as_choices',
        'birth_year', 'is_active', 'show_work_count', )
    list_filter = ('generation_as_choices', 'is_active')
    list_editable = ['is_active']
    readonly_fields = ['sidar_id', ]
    fields = ['name', 'sidar_id', 'birth_year', 'death_year',
              'birth_country', 'generation_as_choices', 'belongs_to_studio',
              'photo', 'philosophy', 'cv', 'is_active', 'philosophy_summary']


class CollectorAdmin(LargeImagePreviewInChangeForm,
                     WithWorkCountField, TranslationAdmin):
    list_display = ('name', 'main_discipline',
                    'birth_year', 'is_active', 'show_work_count',)
    list_filter = ['is_active', ]
    fields = ['name', 'birth_year', 'death_year', 'birth_country', 'homepage',
              'photo', 'philosophy', 'cv', 'is_active', 'philosophy_summary']


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile


class UserAdmin(UserAdmin):
    search_fields = ()
    list_filter = ()
    inlines = (UserProfileInline, )
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'is_active', 'is_staff', 'is_superuser', 'get_designers')

    def get_designers(self, instance):
        names = [
            item.name for item in instance.get_profile().in_charge_of_designers.all()
        ]
        return ', '.join(names)
    get_designers.short_description = u'מעצבים בטיפול'


class CategorySubjectModelAdmin(WithWorkCountField, TranslationAdmin):
    list_display = ['name', 'parent', 'main_discipline',
                    'info', 'show_work_count']
    list_filter = ['parent']

admin.site.register(models.Category, CategorySubjectModelAdmin)
admin.site.register(models.Subject, CategorySubjectModelAdmin)
admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.Designer, DesignerAdmin)
admin.site.register(models.Discipline, DisciplineAdmin)
admin.site.register(models.Collector, CollectorAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
