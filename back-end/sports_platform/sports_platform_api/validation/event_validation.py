from rest_framework import serializers

class Event(serializers.Serializer):

    name = serializers.CharField(min_length=2, max_length=100, required=True)
    sport = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

    startDate = serializers.DateTimeField(format='iso-8601', required=True)

    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, max_value=90, min_value=-90, required=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, max_value=180, min_value=-180, required=True)

    minimumAttendeeCapacity = serializers.IntegerField(min_value=0, required=True)
    maximumAttendeeCapacity = serializers.IntegerField(min_value=1, required=True)
    maxSpectatorCapacity = serializers.IntegerField(min_value=0, required=True)
    minSkillLevel = serializers.IntegerField(min_value=1, max_value=5, required=True)
    maxSkillLevel = serializers.IntegerField(min_value=1, max_value=5, required=True)
    acceptWithoutApproval = serializers.BooleanField(required=True)

    def validate(self, data):

        if data['minSkillLevel'] > data['maxSkillLevel']:
            raise serializers.ValidationError({"skillLevel": "minSkillLevel should be smaller than or equal to maxSkillLevel"})

        if not data['startDate'].time():
            raise serializers.ValidationError({"time": "startDate should include time"})

        return data

class Request_Message(serializers.Serializer):
    message = serializers.CharField(required=False)

class Accept_Participant(serializers.Serializer):
    accept_user_id_list = serializers.ListField(
        child=serializers.IntegerField(
            min_value=0, max_value=9223372036854775807)
    )
    reject_user_id_list = serializers.ListField(
        child=serializers.IntegerField(
            min_value=0, max_value=9223372036854775807)
    )
