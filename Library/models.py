from django.db import models
from django.contrib.auth.models import *
 
# Create your models here. 
class Author(models.Model): 
    name = models.CharField(max_length=100, unique=True) 
    
    def __str__(self):
        return self.name;
    
    class Meta:
        ordering = ['name']
 
class Tag(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
 
    def __str__(self):
        return self.name;
    
    class Meta:
        ordering = ['name']
 
class Genre(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
 
    def __str__(self):
        return self.name;
    
    class Meta:
        ordering = ['name']

 
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title', unique=True)
    authors = models.ManyToManyField(Author, verbose_name='Authors')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    coverart = models.ImageField(upload_to="images/", default="", verbose_name='Image')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

