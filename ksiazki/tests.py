from django.test import TestCase
from django.test import Client
from django.urls import reverse
import pytest
from ksiazki.models import Publisher, Category, Book, Author
from ksiazki.forms import AddBookForm, AddAuthorForm
import datetime


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_publisher_list(marchewka):
#     client = Client()
#     url = reverse('publishers')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['context'].count() == len(marchewka)
#     for p in marchewka:
#         assert p in response.context['context']


@pytest.mark.django_db
def test_category_list(categories):
    client = Client()
    url = reverse('categories')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['context'].count() == len(categories)
    for c in categories:
        assert c in response.context['context']


@pytest.mark.django_db
def test_add_publisher_get():
    client = Client()
    url = reverse('add_publisher')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_publisher_get():
    client = Client()
    url = reverse('add_publisher')
    data = {
        'name': 'ppp'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    # redirect_url = reverse('add_publisher')
    # assert response.url.startswith(redirect_url)
    Publisher.objects.get(name='ppp')


@pytest.mark.django_db
def test_add_category_get():
    client = Client()
    url = reverse('add_category')
    data = {
        'name': 'a'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    Category.objects.get(name='a')


# @pytest.mark.django_db
# def test_add_book(marchewka, categories, authors):
#     client = Client()
#     url = reverse('add_book')
#     data = {
#         'title': 'a',
#         'publisher': marchewka[0].id,
#         'categories': categories[0].id,
#         'author': authors[0].id,
#         'year': 2012
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     redirect_url = reverse('add_book')
#     assert response.url.startswith(redirect_url)
#     Book.objects.get(title='a')


@pytest.mark.django_db
def test_add_book_get():
    client = Client()
    url = reverse('add_book')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddBookForm)


@pytest.mark.django_db
def test_add_book_post(authors, marchewka, categories):
    client = Client()
    url = reverse('add_book')
    data = {
        'title': 'a',
        'publisher': marchewka[0].id,
        'categories': [c.id for c in categories],
        'author': authors[0].id,
        'year': 2012
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('add_book'))
    Book.objects.get(title='a')


@pytest.mark.django_db
def test_add_book_post_less_than_birth_date(authors, marchewka, categories):
    client = Client()
    url = reverse('add_book')
    data = {
        'title': 'a',
        'publisher': marchewka[0].id,
        'categories': [c.id for c in categories],
        'author': authors[0].id,
        'year': 123
    }
    response = client.post(url, data)
    assert response.status_code == 200
    try:
        Book.objects.get(title='a')
        assert False
    except Book.DoesNotExist:
        assert True
    form = response.context['form']
    assert isinstance(form, AddBookForm)
    assert 'Nie mogl napisac tej ksiazki!' == form.errors['__all__'][0]


@pytest.mark.django_db
def test_edit_author_get(authors):
    client = Client()
    url = reverse('edit_author', kwargs={'id': authors[0].id})
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddAuthorForm)


@pytest.mark.django_db
def test_edit_author_post(authors):
    client = Client()
    url = reverse('edit_author', kwargs={'id': authors[0].id})
    data = {
        'first_name': 'Jim',
        'last_name': 'Beam',
        'date': '2014-05-05',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('authors'))
    a = Author.objects.get(first_name='Jim')
    assert a.id == authors[0].id


@pytest.mark.django_db
def test_book_list_view_not_login():
    client = Client()
    url = reverse('books')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_book_list_view_login_without_permission(user):
    client = Client()
    client.force_login(user)
    url = reverse('books')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_book_list_view_login_with_permission(user_with_permission_for_view_book):
    client = Client()
    client.force_login(user_with_permission_for_view_book)
    url = reverse('books')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_publishers_list_view_not_login():
    client = Client()
    url = reverse('publishers')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_publishers_list_view_login_without_permission(user):
    client = Client()
    client.force_login(user)
    url = reverse('publishers')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_publishers_list_view_login_with_permission(user_with_permission_for_view_publishers):
    client = Client()
    client.force_login(user_with_permission_for_view_publishers)
    url = reverse('publishers')
    response = client.get(url)
    assert response.status_code == 200
