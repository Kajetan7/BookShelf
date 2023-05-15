from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=128)


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()

