from .models import *
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class ChangeElementForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), 
                                             label='Authors', 
                                             widget=forms.CheckboxSelectMultiple())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          label='Tags', 
                                          widget=forms.CheckboxSelectMultiple())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), 
                                            label='Genres', 
                                            widget=forms.CheckboxSelectMultiple())
    coverart = forms.ImageField(label='Cover Art', 
                                widget=forms.ClearableFileInput(attrs={'style' : 'border: 1px solid #ccc; border-radius: 5px; padding: 10px; font-size: 16px;', }))

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
                                            'class': 'form-control',
                                            'style': 'width: 100%;',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 
                                                 'rows': '7', 
                                                 'style': 'resize: none;'})
        }

class ChangeAuthor(forms.ModelForm):
    name = forms.CharField(label="Full Name", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                        'class': 'form-control', 
                                                        'style': 'width: 100%;', }),)
    
    class Meta:
        model = Author
        fields = ('name', )
        
class ChangeTag(forms.ModelForm):
    name = forms.CharField(label="Tag", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                         'class': 'form-control', 
                                                         'style': 'width: 100%;',}),)
    
    class Meta:
        model = Tag
        fields = ('name', )

class ChangeGenre(forms.ModelForm):
    name = forms.CharField(label="Genre", 
                           widget=forms.TextInput(attrs={'type': 'text', 
                                                         'class': 'form-control', 
                                                         'style': 'width: 100%;',}),)
    
    class Meta:
        model = Genre
        fields = ('name', )
        
class SearchForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), 
                                             label='Authors', 
                                             widget=forms.CheckboxSelectMultiple(attrs={'name': 'authors',}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), 
                                          label='Tags', 
                                          widget=forms.CheckboxSelectMultiple(attrs={'name' : 'tags',}))
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), 
                                            label='Genres', 
                                            widget=forms.CheckboxSelectMultiple(attrs={'name' : 'genres',}))
    coverart = forms.ImageField(label='Cover Art', 
                                widget=forms.FileInput(attrs={'style' : 'border: 1px solid #ccc; border-radius: 5px; padding: 10px; font-size: 16px;',}))

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
                                            'class': 'form-control', 
                                            'style': 'width: 30%;', 'name' : 'title',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 
                                                 'rows': '7', 
                                                 'style': 'width: 50%; resize: none;', 
                                                 'name' : 'description',})
        }
        

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', 
                               widget=forms.TextInput(attrs={'class': ' form-control',}))
    email = forms.CharField(label='Email', 
                            widget=forms.TextInput(attrs={'class': ' form-control',}))
    password1 = forms.CharField(label='Password', 
                                widget=forms.TextInput(attrs={'class': ' form-control', 
                                                            'type': 'password',}))
    password2 = forms.CharField(label='Confirm Password', 
                                widget=forms.TextInput(attrs={'class': ' form-control', 
                                                            'type': 'password',}))
    
    class Meta:
        model = User
        fields = ('username', 
                  'email', 
                  'password1', 
                  'password2',)
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username", 
                               widget=forms.TextInput(attrs={'class': ' form-control',}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'class': ' form-control',}))
