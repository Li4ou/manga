from .views import *
from django.urls import path

urlpatterns = [

    path('manga/<str:slug>/chapter/<int:pk_1>-<int:pk_2>/<int:pk_3>/', ChapterView.as_view()),
    path('manga/<str:slug>/', MangaDetailView.as_view(), name='manga'),
    path('catalog', FilterManga.as_view(), name='catalog'),
    path('author/<str:slug>/', AuthorDetailView.as_view(), name='author'),
    path('publisher/<str:slug>/', PublisherDetailView.as_view(), name='publisher'),
    path('painter/<str:slug>/', PainterDetailView.as_view(), name='painter'),
    path('', MainTemplateView.as_view()),

]
