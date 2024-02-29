from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'isbn', 'author', 'publication_year', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        enable_confirmation = cleaned_data.get('enable_confirmation')

        # "Enable Tasdiqlash" belgisini tekshirish
        if enable_confirmation:
            # Tasdiqlash shartini yozing
            pass

        return cleaned_data