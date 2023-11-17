from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy("dashboards:dashboard")


class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy("dashboards:dashboard")
