from django import forms
from .models import Book, OnlineBook, BookLoan


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'book_id', 'author', 'publication_year', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        enable_confirmation = cleaned_data.get('enable_confirmation')

        # "Enable Tasdiqlash" belgisini tekshirish
        if enable_confirmation:
            # Tasdiqlash shartini yozing
            pass

        return cleaned_data


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
