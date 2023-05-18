from django import forms
from django.core.exceptions import ValidationError

from ksiazki.models import Book, Comment


def check_if_upper(value):
    if not value.istitle():
        raise ValidationError("WIelkiei")


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=128, validators=[check_if_upper])
    last_name = forms.CharField(max_length=128)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class AddBookForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data['author']
        year = cleaned_data['year']
        if author.birth_date.year > year:
            raise ValidationError('Nie mogl napisac tej ksiazki!')
        return cleaned_data

    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'categories', 'author', 'year']
        widgets = {
            'categories': forms.CheckboxSelectMultiple
        }


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']