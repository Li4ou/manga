class SlugMixin:
    prepopulated_fields = {'slug': ('name',)}


class TitleMixin:
    list_display = ['__str__', 'get_title_manga']

    def get_title_manga(self, obj):
        return obj.manga
    get_title_manga.short_description = "Тайтл"
