from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.receives.models import Receive
from apps.receives.serializers import ReceiveSerializer


# Create your views here.
class ReceiveViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
