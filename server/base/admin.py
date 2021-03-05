from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'type_manga','get_poster' ]
    prepopulated_fields = {'slug': ('title',)}

    def get_poster(self, obj):
        return mark_safe(f'<img src=/media/{obj.poster} width="50" height="60">')

    get_poster.short_description = "Постер"

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Painter)
class PaniterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Chapter)
admin.site.register(TypeManga)
admin.site.register(ChapterImage)
admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(RaitingStar)
admin.site.register(Rating)
admin.site.register(Tome)

# Register your models here.
