# Generated by Django 3.1.3 on 2021-02-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='autor/', verbose_name='Изображкние')),
            ],
            options={
                'verbose_name': 'Авторы и художники',
                'verbose_name_plural': 'Авторы и художники',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Катигории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('urls', models.SlugField(max_length=160)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('urls', models.SlugField()),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='poster/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=0, verbose_name='Дата выхода')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Дата добавления')),
                ('transfer_status', models.CharField(choices=[('0', 'Продолжаеться'), ('1', 'Завершен'), ('2', 'Замарожен'), ('3', 'Заброшен')], default='1', max_length=10)),
                ('title_status', models.CharField(choices=[('0', 'Продолжаеться'), ('1', 'Завершен'), ('2', 'Замарожен'), ('3', 'Заброшен')], default='0', max_length=10)),
                ('author', models.ManyToManyField(to='base.Author', verbose_name='Автор')),
                ('genres', models.ManyToManyField(to='base.Genres', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
            },
        ),
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='painter/', verbose_name='Изображкние')),
            ],
            options={
                'verbose_name': 'Художник',
                'verbose_name_plural': 'Художники',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='publisher/', verbose_name='Изображкние')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='RaitingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='TypeManga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Tome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.manga', verbose_name='Манга')),
            ],
            options={
                'verbose_name': 'Том',
                'verbose_name_plural': 'Том',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.manga', verbose_name='Манга')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.raitingstar', verbose_name='Звёзды')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
        migrations.AddField(
            model_name='manga',
            name='painter',
            field=models.ManyToManyField(to='base.Painter', verbose_name='Художник'),
        ),
        migrations.AddField(
            model_name='manga',
            name='publisher',
            field=models.ManyToManyField(to='base.Publisher', verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='manga',
            name='type_manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.typemanga'),
        ),
        migrations.CreateModel(
            name='ChapterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chapter')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='tom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tome'),
        ),
    ]
