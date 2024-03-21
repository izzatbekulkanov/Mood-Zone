from django.urls import path
from .views import logout_view, OAuthAuthorizationView, OAuthCallbackView

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('oauth2/authorize/', OAuthAuthorizationView.as_view(), name='oauth_authorize'),
    path('oauth2/callback', OAuthCallbackView.as_view(), name='oauth_callback'),
]
