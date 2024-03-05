from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    # URL pattern for the index page
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # API endpoints for authentication using Djoser
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('djoser.urls.jwt')),

    # URL pattern for allauth
    path('auth/', include('allauth.urls')),

    # URL pattern for logging out
    path('logout/', LogoutView.as_view(), name='logout'),

    # URL pattern for Google authentication
    path('accounts/google/', include('allauth.socialaccount.urls')),

    # URL pattern for Facebook authentication
    path('accounts/facebook/', include('allauth.socialaccount.urls')),
]
