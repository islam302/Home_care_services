from django.contrib import admin
from django.urls import path, include
from .views import EmployeeViewSet, ContactViewSet, ClientViewSet, ServicesViewSet, CustomerReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Employee', EmployeeViewSet, basename='employee')
router.register('Clients', ClientViewSet, basename='client')
router.register('ContactUs', ContactViewSet, basename='ContactUs')
router.register('Services', ServicesViewSet, basename='Services')
router.register('Customer-reviews', CustomerReviewViewSet, basename='reviews')

urlpatterns = router.urls
