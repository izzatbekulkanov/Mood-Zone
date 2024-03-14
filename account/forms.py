from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Permission, Group
from .models import CustomGroup, CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number')

class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CustomGroup
        fields = ['name', 'permissions']

class UserProfileForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'groups']