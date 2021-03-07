from .utils import *

from .models import *
from django.contrib import admin
from django.utils.safestring import mark_safe


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'type_manga', 'get_poster']
    prepopulated_fields = {'slug': ('title',)}

    def get_poster(self, obj):
        return mark_safe(f'<img src=/media/{obj.poster} width="50" height="60">')

    get_poster.short_description = "Постер"


@admin.register(Author)
class AuthorAdmin(SlugMixin, admin.ModelAdmin): pass


@admin.register(Publisher)
class PublisherAdmin(SlugMixin, admin.ModelAdmin): pass


@admin.register(Painter)
class PaniterAdmin(SlugMixin, admin.ModelAdmin): pass


@admin.register(Tome)
class PaniterAdmin(TitleMixin,admin.ModelAdmin):pass


@admin.register(Chapter)
class ChapterAdmin(TitleMixin,admin.ModelAdmin):
    def get_title_manga(self, obj):
        return obj.tom.manga

@admin.register(ChapterImage)
class ChapterAdmin(TitleMixin,admin.ModelAdmin):
    def get_title_manga(self, obj):
        return obj.chapter.tom.manga



admin.site.register(TypeManga)
admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(RaitingStar)
admin.site.register(Rating)

# Register your models here.
