from django import forms
from django.contrib.auth.hashers import check_password


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(label='Avvalgi Parol', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Yangi Parol', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Yangi Parolni Tasdiqlash', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not check_password(current_password, self.user.password):
            raise forms.ValidationError("Noto'g'ri parol")
        return current_password

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError("Yangi parollar mos kelmadi")
        return confirm_new_password