from rest_framework import serializers

from .models import Info


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Info
