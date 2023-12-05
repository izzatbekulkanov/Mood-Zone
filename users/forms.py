# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required add a valid email address")
    first_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')

        # Check if the password is too similar to the email
        if email and password:
            if password.lower().find(email.lower()) != -1:
                raise ValidationError("The password is too similar to the email.")

        validate_password(password)

        # Check if the password is too similar to the first name
        if first_name and password.lower().find(first_name.lower()) != -1:
            raise ValidationError("The password is too similar to the first name.")

        return password

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')

        # Check if the passwords match
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return password2

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(f"Username {username} is already in use")