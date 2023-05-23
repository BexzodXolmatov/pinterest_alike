from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from account.serializers import CustomTokenObtainPairSerializer
from rest_framework import generics

from account.serializers import RegisterSerializer
from account.models import User


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
