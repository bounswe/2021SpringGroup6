from rest_framework import serializers
from .generic_validators import english_dot_number

class Search(serializers.Serializer):
    creator = serializers.IntegerField(min_value=1, required=False)
    nameContains = serializers.CharField(required=False)
    
    latitudeBetweenStart = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=90, min_value=-90, required=False)
    latitudeBetweenEnd = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=90, min_value=-90, required=False)
    longitudeBetweenStart = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=180, min_value=-180, required=False)
    longitudeBetweenEnd = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=180, min_value=-180, required=False)
    
    sport = serializers.CharField(required=False)

    def validate(self, data):
        if ((('latitudeBetweenStart' in data) and ('latitudeBetweenEnd' not in data)) or ('latitudeBetweenStart' not in data) and (('latitudeBetweenEnd' in data))):
            raise serializers.ValidationError(
                {"latitude": "latitudeBetweenStart and latitudeBetweenEnd must be given together."})

        if ((('longitudeBetweenStart' in data) and ('longitudeBetweenEnd' not in data)) or ('longitudeBetweenStart' not in data) and (('longitudeBetweenEnd' in data))):
            raise serializers.ValidationError(
                {"longitude": "longitudeBetweenStart and longitudeBetweenEnd must be given together."})

        return data


class Equipment(serializers.Serializer):

    name = serializers.CharField(min_length=2, max_length=100, required=True)
    sport = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    sharedContent = serializers.URLField(required=False)

    latitude = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=90, min_value=-90, required=True)
    longitude = serializers.DecimalField(
        max_digits=9, decimal_places=6, max_value=180, min_value=-180, required=True)


class EquipmentDiscussionPost(serializers.Serializer):
    sharedContent = serializers.URLField(required=False)
    text = serializers.CharField(required=True)


class EquipmentDiscussionComment(serializers.Serializer):
    text = serializers.CharField(required=False)
