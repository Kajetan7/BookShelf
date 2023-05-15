from django.shortcuts import render, redirect
from django.views import View
from ksiazki.models import Publisher, Category, Author
from ksiazki.forms import AddAuthorForm


class IndexView(View):
    def get(self, request):
        context = {
            'context': 'Bookshelf'
        }
        return render(request, 'ksiazki/index.html', context)


class Publishers(View):
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