from rest_framework import serializers

class NewBadge(serializers.Serializer):
    sport = serializers.CharField(required=False)
    description = serializers.CharField(required=True)
