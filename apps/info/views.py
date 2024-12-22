from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from .models import Info
from .serializers import InfoSerializer


class InfoModelViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
