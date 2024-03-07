from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('djoser.urls.jwt')),
    path('auth/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/google/', include('allauth.socialaccount.urls')),
    path('accounts/facebook/', include('allauth.socialaccount.urls')),
]
