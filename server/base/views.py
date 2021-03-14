import datetime

# from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
# from django.db.models import Q
from .models import (Manga, Author, Publisher,
                     Painter, TypeManga, Genres,
                     TitleStatus, TransferStatus)

# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
#
# import logging

CACHE_TTL = 60 * 5


class Data:
    @staticmethod
    def get_genres():
        return Genres.objects.all()

    @staticmethod
    def get_type():
        return TypeManga.objects.all()

    @staticmethod
    def get_title_status():
        return TitleStatus.objects.all()

    @staticmethod
    def get_transfer_status():
        return TransferStatus.objects.all()


class FilterManga(Data, ListView):
    """СТраница каталога"""
    model = Manga
    template_name = 'catalog.html'
    paginate_by = 30
    ordering = ['id']

    def get_queryset(self):
        name = self.request.GET.get('name', False)
        if not name:
            queryset = Manga.objects.filter(
                genres__in=self.request.GET.getlist('genres', [0, 1, 2, 3]),
                type_manga__in=self.request.GET.getlist('type', [1, 2, 3, ]),
                transfer_status__in=self.request.GET.getlist('transfer_status', [0, 1, 2, 3]),
                title_status__in=self.request.GET.getlist('title_status', [0, 1, 2, 3])).distinct()

        else:
            queryset = Manga.objects.filter(title__contains=name)
        return queryset

    def get_context_data(self, **kwargs):
        urls = str()
        filter_parameters = dict()
        if self.request.GET:
            for key in self.request.GET:
                if key != 'page':
                    filter_parameters[key] = [int(item) for item in self.request.GET.getlist(key)]
                    for value in self.request.GET.getlist(key):
                        urls += f"{key}={value}&"

        context = {'urls': urls,
                   'filter_parameters': filter_parameters}

        return super().get_context_data(**context)


class MainTemplateView(TemplateView):
    """Главная страница
    {
    manga_top: list,
    manga_hot: list,
    chapter_updates: list,
    }
    """

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        manga_top = Manga.objects.all().order_by("rating")[:20]
        manga_hot = Manga.objects.prefetch_related('genres').filter(
            data__range=[now - datetime.timedelta(7), now])[:20]
        context = {
            'manga_top': manga_top,
            'manga_hot': manga_hot
        }
        # context['chapter_updates'] = Chapter.objects.select_related('manga').all().distinct('manga')[:20]
        return super().get_context_data(**context)


#
# @method_decorator(cache_page(CACHE_TTL), name='get')
class MangaDetailView(DetailView):
    """Описание  манги"""
    model = Manga
    template_name = 'manga.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['toms'] = self.object.tome_set.all()
        return context


# @method_decorator(cache_page(CACHE_TTL), name='get')
class ChapterView(DetailView):
    """Чтение манги"""
    model = Manga
    template_name = 'chapters.html'

    def get_context_data(self, **kwargs):
        tome = self.object.tome_set.filter(number=kwargs["pk_1"])[0]
        chapter = tome.chapter_set.filter(number=kwargs["pk_2"])[0]
        image = chapter.chapterimage_set.get(number=kwargs["pk_3"])
        context = {
            'tome': tome,
            'chapter': chapter,
            'image': image
        }
        return super().get_context_data(**context)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, **kwargs)
        response = self.render_to_response(context)
        return response


class DataDetalView(DetailView):
    """Вывод информации"""
    template_name = 'author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manga'] = self.object.manga_set.all()
        return context


class AuthorDetailView(DataDetalView):
    """Вывод информации о авторе"""
    model = Author


class PainterDetailView(DataDetalView):
    """Вывод информации о художнике"""
    model = Painter


class PublisherDetailView(DataDetalView):
    """Вывод информации  о издателе"""
    model = Publisher
