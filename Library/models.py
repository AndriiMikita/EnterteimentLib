from django.db import models
from django.contrib.auth.models import *
 
# Create your models here. 
class Author(models.Model): 
    name = models.CharField(max_length=100, unique=True) 
    
    def __str__(self):
        return self.name;
 
class Tag(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
 
    def __str__(self):
        return self.name;
 
class Genre(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
 
    def __str__(self):
        return self.name;

 
class Book(models.Model): 
    title = models.CharField(max_length=200, verbose_name='Назва', unique=True, on_delete=models.CASCADE) 
    authors = models.ManyToManyField(Author, verbose_name='Автори', on_delete=models.CASCADE) 
    tags = models.ManyToManyField(Tag, verbose_name='Теги', on_delete=models.CASCADE) 
    genres = models.ManyToManyField(Genre, verbose_name='Жанри', on_delete=models.CASCADE) 
    coverart = models.ImageField(upload_to="images/", default="", verbose_name='Зображення', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Опис')
    
    def __str__(self):
        return self.title;