from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Info
from .serializers import InfoSerializer


class InfoModelViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
