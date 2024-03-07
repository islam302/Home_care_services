from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, ContactUs, Client, Services, CustomerReviews
from .serializers import EmployeeSerializer, CustomReviewSerializer, ClientSerializer, ContactUsSerializer, ServicesSerializer
from rest_framework.decorators import action


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset
        else:
            return Employee.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.is_authenticated:
            return Response(serializer.data)
        else:
            login_url = 'http://127.0.0.1:8000/auth/api/jwt/create'
            signup_url = 'http://127.0.0.1:8000/auth/api/users/'
            message = f'You are not authenticated. Please Login from here : "{login_url}"and Sign up from here "{signup_url}"'
            return Response({'message': message}, status=status.HTTP_401_UNAUTHORIZED)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset
        else:
            return Employee.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.is_authenticated:
            return Response(serializer.data)
        else:
            login_url = 'http://127.0.0.1:8000/auth/api/jwt/create'
            signup_url = 'http://127.0.0.1:8000/auth/api/users/'
            message = f'You are not authenticated. Please Login from here : "{login_url}"and Sign up from here "{signup_url}"'
            return Response({'message': message}, status=status.HTTP_401_UNAUTHORIZED)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReviews.objects.all()
    serializer_class = CustomReviewSerializer


