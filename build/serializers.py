from rest_framework import serializers
from .models import flowers

class FlowersSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'botanical_name',
            'description',
        )
        model = flowers