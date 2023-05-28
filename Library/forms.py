from .models import *
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class ChangeElementForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), 
                                             label='Автори', 
                                             widget=forms.CheckboxSelectMultiple())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          label='Теги', 
                                          widget=forms.CheckboxSelectMultiple())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), 
                                            label='Жанри', 
                                            widget=forms.CheckboxSelectMultiple())
    coverart = forms.ImageField(label='Обкладинка', 
                                widget=forms.FileInput(attrs={'style' : 'border: 1px solid #ccc; border-radius: 5px; padding: 10px; font-size: 16px;', 
                                                              'class' : 'mx-ms-3',}))

    class Meta:
        model = Book
        fields = ('title', 
                  'authors', 
                  'tags', 
                  'genres', 
                  'coverart', 
                  'description')
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text', 
                                            'class': 'form-control mx-sm-3', 
                                            'style': 'width: 30%;'}),
            'description': forms.Textarea(attrs={'class': 'form-control mx-sm-3', 
                                                 'rows': '7', 
                                                 'style': 'width: 50%; resize: none;'})
        }

class ChangeAuthor(forms.ModelForm):
    name = forms.CharField(label="Повне ім'я", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                        'class': 'form-control mx-sm-3', 
                                                        'style': 'width: 30%;', }),)
    
    class Meta:
        model = Author
        fields = ('name', )
        
class ChangeTag(forms.ModelForm):
    name = forms.CharField(label="Тег", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                         'class': 'form-control mx-sm-3', 
                                                         'style': 'width: 30%;',}),)
    
    class Meta:
        model = Tag
        fields = ('name', )

class ChangeGenre(forms.ModelForm):
    name = forms.CharField(label="Жанр", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                         'class': 'form-control mx-sm-3', 
                                                         'style': 'width: 30%;',}),)
    
    class Meta:
        model = Genre
        fields = ('name', )
        
class SearchForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автори', widget=forms.CheckboxSelectMultiple(attrs={'name': 'authors',}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Теги', widget=forms.CheckboxSelectMultiple(attrs={'name' : 'tags',}))
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанри', widget=forms.CheckboxSelectMultiple(attrs={'name' : 'genres',}))
    coverart = forms.ImageField(label='Обкладинка', widget=forms.FileInput(attrs={'style' : 'border: 1px solid #ccc; border-radius: 5px; padding: 10px; font-size: 16px;', 'class' : 'mx-ms-3',}))

    class Meta:
        model = Book
        fields = ('title', 'authors', 'tags', 'genres', 'coverart', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text', 'class': 'form-control mx-sm-3', 'style': 'width: 30%;', 'name' : 'title',}),
            'description': forms.Textarea(attrs={'class': 'form-control mx-sm-3', 'rows': '7', 'style': 'width: 50%; resize: none;', 'name' : 'description',})
        }
        

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': ' form-control mx-sm-3'}))
    email = forms.CharField(label='Пошта', widget=forms.TextInput(attrs={'class': ' form-control mx-sm-3'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': ' form-control mx-sm-3', 'type': 'password'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.TextInput(attrs={'class': ' form-control mx-sm-3', 'type': 'password'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={'class': ' form-control mx-sm-3'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': ' form-control mx-sm-3'}))