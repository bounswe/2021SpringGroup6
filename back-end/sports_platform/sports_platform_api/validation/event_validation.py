from rest_framework import serializers

class Event(serializers.Serializer):

    name = serializers.CharField(min_length=2, max_length=100, required=True)
    sport = serializers.CharField(required=True)
    description = models.CharField(required=False)

    startDate = models.DateTimeField(format='iso-8601', required=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, required=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, required=True)

    minimumAttendeeCapacity = models.IntegerField(min_value=0, required=True)
    maximumAttendeeCapacity = models.IntegerField(min_value=1, required=True)
    maxSpectatorCapacity = models.IntegerField(min_value=0, required=True)
    minSkillLevel = models.IntegerField(min_value=1, max_value=5, required=True)
    maxSkillLevel = models.IntegerField(min_value=1, max_value=5, required=True)

    def validate(self, data):

        if data['minSkillSevel'] > data['maxSkillSevel']:
            raise serializers.ValidationError("minSkillLevel should be smaller than or equal to maxSkillLevel")

        if not (data['startDate'].contains('T') or data['startDate'].contains('t')):
            raise serializers.ValidationError("startDate should include time")

        return data
