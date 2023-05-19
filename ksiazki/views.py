from django.shortcuts import render, redirect
from django.views import View
from ksiazki.models import Publisher, Category, Author, Book, Comment
from ksiazki.forms import AddAuthorForm, AddBookForm, AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


class IndexView(View):
    def get(self, request):
        context = {
            'context': 'Bookshelf'
        }
        return render(request, 'ksiazki/index.html', context)


class Publishers(PermissionRequiredMixin, View):
    permission_required = ['ksiazki.view_permission']

    def get(self, request):
        publishers = Publisher.objects.all()
        context = {
            'context': publishers
        }
        return render(request, 'ksiazki/publishers.html', context)


class Authors(View):
    def get(self, request):
        authors = Author.objects.all()
        context = {
            'context': authors
        }
        return render(request, 'ksiazki/authors.html', context)


class AddPublisher(View):
    def get(self, request):
        return render(request, 'ksiazki/add_publisher.html')

    def post(self, request):
        name = request.POST.get('name')
        Publisher.objects.create(name=name)
        context = {
            'context': 'Publisher has been created'
        }
        return render(request, 'ksiazki/add_publisher.html', context)


class EditPublisher(View):
    def get(self, request, id):
        publisher = Publisher.objects.get(id=id)
        context = {
            'publisher': publisher
        }
        return render(request, 'ksiazki/edit_publisher.html', context)

    def post(self, request, id):
        new_name = request.POST.get('name')
        publisher_name = Publisher.objects.get(id=id)
        publisher_name.name = new_name
        publisher_name.save()
        return redirect('/books/publishers/')


class Categories(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'context': categories
        }
        return render(request, 'ksiazki/categories.html', context)


class AddCategory(View):
    def get(self, request):
        return render(request, 'ksiazki/add_category.html')

    def post(self, request):
        name = request.POST.get('name')
        Category.objects.create(name=name)
        context = {
            'context': 'Category has been created'
        }
        return render(request, 'ksiazki/add_category.html', context)


class EditCategory(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        context = {
            'category': category
        }
        return render(request, 'ksiazki/edit_category.html', context)

    def post(self, request, id):
        new_name = request.POST.get('name')
        category_name = Category.objects.get(id=id)
        category_name.name = new_name
        category_name.save()
        return redirect('/books/categories/')


class AddAuthorView(View):

    def get(self, request):
        form = AddAuthorForm()
        return render(request, 'ksiazki/add_author.html', {'form': form})

    def post(self, request):
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            Author.objects.create(first_name=first_name, last_name=last_name, birth_date=date)
            return redirect('add_author')
        return render(request, 'ksiazki/add_author.html', {'form': form})


class EditAuthor(View):
    def get(self, request, id):
        form = AddAuthorForm()
        return render(request, 'ksiazki/edit_author.html', {'form': form})

    def post(self, request, id):
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_birth_date = form.cleaned_data['date']

            author = Author.objects.get(id=id)
            author.first_name = new_first_name
            author.last_name = new_last_name
            author.birth_date = new_birth_date
            author.save()

            return redirect('authors')
        return render(request, 'ksiazki/edit_author.html', {'form': form})


class AddBookView(View):

    def get(self, request):
        form = AddBookForm()
        return render(request, 'ksiazki/add_book.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
        return render(request, 'ksiazki/add_book.html', {'form': form})


class Books(PermissionRequiredMixin, View):
    permission_required = ['ksiazki.view_book']

    def get(self, request):
        books = Book.objects.all()
        context = {
            'context': books
        }
        return render(request, 'ksiazki/books.html', context)


class BookDetails(LoginRequiredMixin, View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        form = AddCommentForm()
        context = {
            'book': book,
            'form': form
        }
        return render(request, 'ksiazki/book_details.html', context)

    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('index')
        book = Book.objects.get(id=id)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect('book_details', id)
        return render(request, 'ksiazki/book_details.html', {'book': book, 'form': form})


class EditCommentView(UserPassesTestMixin, View):

    def test_func(self):
        comment = Comment.objects.get(id=self.kwargs['pk'])
        return comment.user == self.request.user

    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        form = AddCommentForm(instance=comment)
        return render(request, 'book_generic/form.html', {'form': form})
