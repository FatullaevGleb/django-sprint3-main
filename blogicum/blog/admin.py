from django.contrib import admin

from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    """Админ-панель для модели Post"""

    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = (
        'category',
        'location',
        'is_published',
    )
    search_fields = (
        'title',
        'text',
        'location',
        'pub_date',
        'author',
    )
    list_filter = ('category',)
    list_display_links = ('title',)
    ordering = ('-pub_date',)


class CategoryAdmin(admin.ModelAdmin):
    """Админ-панель для модели Category."""

    list_display = (
        'title',
        'slug',
        'created_at',
        'is_published',
    )
    list_editable = ('is_published',)
    list_filter = ('title',)


class LocationAdmin(admin.ModelAdmin):
    """Админ-панель для модели Location."""

    list_display = (
        'name',
        'created_at',
        'is_published',
    )
    list_editable = ('is_published',)
    list_filter = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
