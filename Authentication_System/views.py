from django.conf import settings
from django.shortcuts import render
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
