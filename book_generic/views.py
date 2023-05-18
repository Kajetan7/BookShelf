from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from ksiazki.models import Book, Author, Publisher


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'book_generic/list_view.html'

class AddBookGenericView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_generic/form.html'

class AuthorGenericListView(ListView):
    model = Author
    template_name = 'book_generic/list_view.html'


class PublisherGenericListView(ListView):
    model = Publisher
    template_name = 'book_generic/list_view.html'


class AddPublisherGenericView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'book_generic/form.html'


class UpdatePublisherGenericView(UpdateView):
    model = Publisher
    template_name = 'book_generic/form.html'
    fields = '__all__'
