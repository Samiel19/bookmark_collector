# Generated by Django 4.2.7 on 2023-11-15 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='Ссылка', max_length=2000, unique=True, verbose_name='Ссылка')),
                ('title', models.CharField(blank=True, editable=False, help_text='Название закладки', max_length=150, verbose_name='Название')),
                ('type', models.CharField(blank=True, editable=False, help_text='Тип закладки', max_length=150, verbose_name='Тип')),
                ('description', models.TextField(blank=True, editable=False, help_text='Описание закладки', verbose_name='Описание')),
                ('image', models.URLField(blank=True, editable=False, max_length=2000, verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор закладки')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('name', models.CharField(help_text='Название коллекции закладок', max_length=150, unique=True, verbose_name='Имя коллекции')),
                ('description', models.CharField(help_text='Описание коллекции закладок', max_length=500, verbose_name='Описание коллекции')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец коллекции')),
                ('link', models.ManyToManyField(blank=True, to='bookmark.bookmark', verbose_name='Закладка')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
                'ordering': ('-created_at',),
                'default_related_name': 'collection',
            },
        ),
    ]
