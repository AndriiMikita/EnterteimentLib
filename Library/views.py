from django.shortcuts import render, redirect
from django.urls import *
from .models import *   
from .forms import *
from .filters import *
from django.views.generic import *
from django_filters.views import *
from django.contrib.auth.views import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from .util import *

# Create yviews here.

class Library(FilterView, DataMixin):
    model = Book
    template_name = 'library/library.html'
    filterset_class = BookFilter
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        context['tags_ids'] = Tag.objects.all().values_list('pk', flat=True)
        return context

    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=Book.objects.all())
        return self.filterset.qs

def edit(request, title):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Creator').exists():
        return redirect('library')
        
    book = Book.objects.filter(title=title).first()

    if request.method == 'POST':
        form = ChangeElementForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show', title=book.title)
        else:
            errors = form.errors
            for field, error_msgs in errors.items():
                for error_msg in error_msgs:
                    print(f"Помилка у полі {field}: {error_msg}")
    else:
        form = ChangeElementForm(instance=book)

    return render(request, "library/edit.html", {
        "book": book,
        "authors": Author.objects.all(),
        "tags": Tag.objects.all(),
        "genres": Genre.objects.all(),
        "form": form,
        "header": 'Редагувати книгу',
        'authenticated' : request.user.is_authenticated,
        'user' : request.user
    })
   
def addBook(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Creator').exists():
        return redirect('library')
    
    book = Book()
    
    if request.method == 'POST':
        form = ChangeElementForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show', title=book.title)
        else:
            errors = form.errors
            for field, error_msgs in errors.items():
                for error_msg in error_msgs:
                    print(f"Помилка у полі {field}: {error_msg}")
    else:
        form = ChangeElementForm(instance=book)
    
    return render(request, "library/add.html", {
        "book": book,
        "authors": Author.objects.all(),
        "tags": Tag.objects.all(),
        "genres": Genre.objects.all(),
        "form": form,
        "header": 'Додати книгу',
        'authenticated' : request.user.is_authenticated,
        'user' : request.user,
    })


def show(request, title):
     return render(request, "library/show.html", {
        "book": Book.objects.filter(title=title).first(),
        'authenticated' : request.user.is_authenticated,
        'user' : request.user,
    })

class addAuthor(CreateView, DataMixin):
    
    form_class = ChangeAuthor
    template_name = "library/addAuthor.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)
    
class addTag(CreateView, DataMixin):
    form_class = ChangeTag
    template_name = "library/addTag.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)
    
class addGenre(CreateView, DataMixin):
    form_class = ChangeGenre
    template_name = "library/addTag.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)
    
class editAuthor(UpdateView, DataMixin):
    model = Author
    form_class = ChangeAuthor
    template_name = "library/editAuthor.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)
    
class editTag(UpdateView, DataMixin):
    model = Tag
    form_class = ChangeTag
    template_name = "library/editTag.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)
    
class editGenre(UpdateView, DataMixin):
    model = Genre
    form_class = ChangeGenre
    template_name = "library/editGenre.html"
    
    def get_success_url(self):
        previous_page = self.request.POST.get('previous_page')
        if previous_page:
            return previous_page
        else:
            return reverse('library')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_page"] = self.request.META.get('HTTP_REFERER')
        context['is_creator'] = self.check_user()
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def check_user(self):
        creator_group = Group.objects.get(name='Creator')
        return creator_group in self.request.user.groups.all()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.check_user():
            return redirect('library')
        return super().dispatch(request, *args, **kwargs)

class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = "user/register.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('library')
        
class LoginUser(LoginView, DataMixin):
    form_class = LoginUserForm
    template_name = "user/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse_lazy('library')
    
def logout_user(request):
    logout(request)
    return redirect('library')