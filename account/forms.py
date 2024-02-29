from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser, BookOrder


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number')
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