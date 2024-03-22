from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/google/', include('allauth.socialaccount.urls')),
    path('accounts/facebook/', include('allauth.socialaccount.urls')),
]