"""
URL configuration for BookShelf_W_13 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ksiazki import views as ksiazki_views
from book_generic import views as book_generic_views


urlpatterns = [
    # path('hello/', ksiazki_views.IndexView.as_view(), name='index'),
    # path('publishers/', ksiazki_views.Publishers.as_view(), name='publishers'),
    # path('add_publisher/', ksiazki_views.AddPublisher.as_view(), name='add_publisher'),
    # path('edit_publisher/<int:id>/', ksiazki_views.EditPublisher.as_view(), name='edit_publisher'),
    # path('categories/', ksiazki_views.Categories.as_view(), name='categories'),
    # path('authors/', ksiazki_views.Authors.as_view(), name='authors'),
    # path('books/', ksiazki_views.Books.as_view(), name='books'),
    # path('books/<int:id>/', ksiazki_views.BookDetails.as_view(), name='book_details'),
    # path('add_category/', ksiazki_views.AddCategory.as_view(), name='add_category'),
    # path('add_author/', ksiazki_views.AddAuthorView.as_view(), name='add_author'),
    # path('add_book/', ksiazki_views.AddBookView.as_view(), name='add_book'),
    # path('edit_category/<int:id>/', ksiazki_views.EditCategory.as_view(), name='edit_category'),
    # path('edit_author/<int:id>/', ksiazki_views.EditAuthor.as_view(), name='edit_author'),
    path('book_gen/', book_generic_views.BookGenericListView.as_view(), name='book_generic_view'),
    path('author_gen/', book_generic_views.AuthorGenericListView.as_view(), name='author_generic_view'),
    path('publisher_gen/', book_generic_views.PublisherGenericListView.as_view(), name='publisher_generic_view'),
    path('add_book/', book_generic_views.AddBookGenericView.as_view(), name='add_book_generic'),
    path('add_publisher/', book_generic_views.AddPublisherGenericView.as_view(), name='add_publisher_generic'),
    path('publisher_gen/<int:pk>/', book_generic_views.UpdatePublisherGenericView.as_view(), name='update_publisher_generic'),
]
