import pytest
from ksiazki.models import Publisher, Category, Author
import datetime
from django.contrib.auth.models import User, Permission


@pytest.fixture
def marchewka():
    lst = []
    lst.append(Publisher.objects.create(name='Ala'))
    lst.append(Publisher.objects.create(name='gosia'))
    lst.append(Publisher.objects.create(name='kasia'))
    return lst


@pytest.fixture
def categories():
    lst = []
    lst.append(Category.objects.create(name='sci-fi'))
    lst.append(Category.objects.create(name='fantasy'))
    lst.append(Category.objects.create(name='action'))
    return lst


@pytest.fixture
def authors():
    lst = []
    lst.append(Author.objects.create(first_name='Zubr', last_name='Piwo1', birth_date=datetime.date(1997, 10, 10)))
    lst.append(Author.objects.create(first_name='Zywiec', last_name='Piwo2', birth_date=datetime.date(1998, 10, 10)))
    lst.append(Author.objects.create(first_name='Wojak', last_name='Piwo3', birth_date=datetime.date(1999, 10, 10)))
    return lst


@pytest.fixture
def user():
    u = User.objects.create(username='qwe')
    return u

@pytest.fixture
def user_with_permission_for_view_book():
    u = User.objects.create(username='qwe')
    perm = Permission.objects.get(codename='view_book')
    u.user_permissions.add(perm)
    return u


@pytest.fixture
def user_with_permission_for_view_publishers():
    u = User.objects.create(username='qwe')
    perm = Permission.objects.get(codename='view_publisher')
    u.user_permissions.add(perm)
    return u