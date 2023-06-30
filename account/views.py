from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import status, permissions, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from account.serializers import RegisterSerializer, UserGetSerializer, UserPostSerializer
from account.models import User


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserGetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(methods=["GET"], detail=False, url_path="profile")
    def profile(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(
        methods=["PUT"],
        detail=False,
        url_path="update-profile",
        serializer_class=UserPostSerializer,
    )
    def update_profile(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)