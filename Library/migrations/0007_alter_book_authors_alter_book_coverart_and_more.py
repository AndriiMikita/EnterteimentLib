# Generated by Django 4.2.1 on 2023-05-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_alter_author_name_alter_book_coverart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='Library.author', verbose_name='Автори'),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverart',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='Library.genre', verbose_name='Жанри'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='Library.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Назва'),
        ),
    ]
