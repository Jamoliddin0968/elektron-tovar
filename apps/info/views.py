from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from .models import Info
from .serializers import InfoSerializer

@extend_schema_view(
    list=extend_schema(tags=["Info"]),
    retrieve=extend_schema(tags=["Info"]),
    create=extend_schema(tags=["Info"]),
    update=extend_schema(tags=["Info"]),
    partial_update=extend_schema(tags=["Info"]),
    destroy=extend_schema(tags=["Info"]),
)
class InfoModelViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
