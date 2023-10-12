from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny


class RegistrationView(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = (
        AllowAny,
    )

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FeedbackView(viewsets.ModelViewSet):
    serializer_class = FeedBackSerializer
    permission_classes = (
        AllowAny,
    )

    def create(self, request):
        serializer = FeedBackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
