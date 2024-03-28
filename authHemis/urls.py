from django.urls import path
from .views import OAuthAuthorizationView, OAuthCallbackView

urlpatterns = [
    path('oauth2/authorize/', OAuthAuthorizationView.as_view(), name='oauth_authorize'),
    path('oauth2/callback', OAuthCallbackView.as_view(), name='oauth_callback'),
]
