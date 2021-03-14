from django.db import models
from django.db.models import signals
from django.shortcuts import reverse
from django.dispatch import receiver


class Category(models.Model):
    """Категории"""
    name = models.CharField('Катигории', max_length=150)
    description = models.TextField('Описание')
    urls = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    """ Авторы"""
    name = models.CharField('Имя', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Изображкние', upload_to='autor/', blank=True, null=True)

    def get_absolute_urls(self):
        return reverse('author', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Авторы и художники'
        verbose_name_plural = 'Авторы и художники'


class Painter(models.Model):
    """ Художники"""
    name = models.CharField('Имя', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Изображкние', upload_to='painter/', blank=True, null=True)

    def get_absolute_urls(self):
        return reverse('painter', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'


class Publisher(models.Model):
    """Издатели"""
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField("Описание")
    image = models.ImageField('Изображкние', upload_to='publisher/', blank=True, null=True)

    def get_absolute_urls(self):
        return reverse('publisher', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Genres(models.Model):
    """Жанры"""
    objects = models.Manager()
    name = models.CharField('Имя', max_length=255)
    description = models.TextField("Описание")
    urls = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def get_absolute_urls(self):
        return f'/catalog?genres={self.id}'


class TypeManga(models.Model):
    """Типы"""
    objects = models.Manager()
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def get_absolute_urls(self):
        return f'/catalog?type={self.id}'


class TransferStatus(models.Model):
    """Статус перевода"""
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Статус перевода'
        verbose_name_plural = 'Статусы перевода'

    def __str__(self):
        return self.name

    def get_absolute_urls(self):
        return f'/catalog?transfer_status={self.id}'


class TitleStatus(models.Model):
    """Статусс тайтла"""
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Статус тайтла'
        verbose_name_plural = 'Статусы тайтла'

    def __str__(self):
        return self.name

    def get_absolute_urls(self):
        return f'/catalog?title_status={self.id}'


class Manga(models.Model):
    """Манга"""
    objects = models.Manager()
    chapter_number = models.IntegerField("Число глав", default=0)
    title = models.CharField('Название', max_length=250)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='poster/')
    author = models.ManyToManyField(Author, verbose_name='Автор')
    painter = models.ManyToManyField(Painter, verbose_name='Художник')
    publisher = models.ManyToManyField(Publisher, verbose_name='Издатель')
    genres = models.ManyToManyField(Genres, verbose_name='Жанры')
    year = models.PositiveSmallIntegerField('Дата выхода', default=0)
    data = models.DateTimeField('Дата добавления', auto_now=True)
    type_manga = models.ForeignKey(TypeManga, on_delete=models.CASCADE, verbose_name='Тип')
    transfer_status = models.ForeignKey(TransferStatus, on_delete=models.CASCADE, verbose_name='Статус перевода',
                                        default=1)
    title_status = models.ForeignKey(TitleStatus, on_delete=models.CASCADE, verbose_name='Статус тайтла', default=1)

    def get_absolute_urls(self):
        return reverse('manga', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'


class Tome(models.Model):
    """Том"""
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    number = models.IntegerField('Номер')

    def __str__(self):
        return f'Том {self.number}'

    class Meta:
        verbose_name = 'Том'
        verbose_name_plural = 'Том'


class Chapter(models.Model):
    """Главы"""
    tom = models.ForeignKey(Tome, on_delete=models.CASCADE, null=True)
    data = models.DateTimeField(auto_now=True)
    number = models.IntegerField('Номер')

    def __str__(self):
        return f" {self.tom} - {self.number}"

    def get_absolute_urls(self):
        return reverse('manga', kwargs={'slug': self.number})

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'


class ChapterImage(models.Model):
    """Страницы"""
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.IntegerField('Номер')
    image = models.ImageField('Изображение')

    def __str__(self):
        return f"{self.chapter}-{self.number}"

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class RaitingStar(models.Model):
    """Звезды рейтинга"""

    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RaitingStar, verbose_name='Звёзды', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.manga}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


@receiver(signals.post_save, sender=Chapter)
def create_customer(sender, instance, **kwargs):
    instance.tom.manga.chapter_number += 1
