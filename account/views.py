from rest_framework.permissions import AllowAny
from rest_framework import generics

from account.serializers import RegisterSerializer
from account.models import User


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
