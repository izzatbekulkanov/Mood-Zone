from django import forms
from .models import Book, OnlineBook, BookLoan, BookOrder


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity', 'publication_year', 'image', 'status']

    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by', None)
        super(BookForm, self).__init__(*args, **kwargs)
        if added_by:
            self.fields['added_by'].initial = added_by

    def save(self, commit=True):
        book = super(BookForm, self).save(commit=False)
        if commit:
            book.save()
        return book


class OnlineBookForm(forms.ModelForm):
    class Meta:
        model = OnlineBook
        fields = ['name', 'content', 'file']  # Model qatorlarini kiritish uchun kerakli maydonlar

    def clean(self):
        cleaned_data = super().clean()
        # Qo'shimcha tekshirishlar shu joyda qo'shilsin
        return cleaned_data


class BookLoanForm(forms.ModelForm):
    class Meta:
        model = BookLoan
        fields = ['book', 'user', 'loan_date', 'status']


class BookOrderForm(forms.ModelForm):
    class Meta:
        model = BookOrder
        fields = ['user', 'book_title', 'author']
        labels = {
            'book_title': 'Kitob nomi',
            'author': 'Muallif nomi'
        }
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        # Qo'shimcha tekshirishlar shu joyda qo'shilsin
        return cleaned_data
