from django import forms
import django_filters
from .models import *

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'type': 'text', 
                                      'class': 'form-control', 
                                      'style': 'width: 100%;',}),
        label="Title",
    )
    authors = django_filters.ModelMultipleChoiceFilter(
        field_name='authors',
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    genres = django_filters.ModelMultipleChoiceFilter(
        field_name='genres',
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Book
        fields = ['title', 'authors', 'tags', 'genres']