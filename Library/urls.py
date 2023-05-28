from django.urls import path
from . import views

# app_name = "library"
urlpatterns = [
    path('', views.Library.as_view(), name="library"),
    path('edit/<str:title>', views.edit, name="edit"),
    path('view/<str:title>', views.show, name="show"),
    path('add/book', views.addBook, name="addBook"),
    path('add/author', views.addAuthor.as_view(), name="addAuthor"),
    path('add/tag', views.addTag.as_view(), name="addTag"),
    path('add/genre', views.addGenre.as_view(), name="addGenre"),
    path('edit/author/<int:pk>', views.editAuthor.as_view(), name="editAuthor"),
    path('edit/tag/<int:pk>', views.editTag.as_view(), name="editTag"),
    path('edit/genre/<int:pk>', views.editGenre.as_view(), name="editGenre"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
 ] 