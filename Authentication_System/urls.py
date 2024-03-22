from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('djoser.urls.jwt')),
    path('auth/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/google/', include('allauth.socialaccount.urls')),
    path('accounts/facebook/', include('allauth.socialaccount.urls')),
]