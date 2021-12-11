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
    duration = serializers.IntegerField(min_value=1, max_value=9223372036854775807)

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


class Search(serializers.Serializer):
    creator = serializers.IntegerField(min_value=1, required=False)
    nameContains = serializers.CharField(required=False)
    timeBetweenStart = serializers.TimeField(format='iso-8601',required=False)
    timeBetweenEnd = serializers.TimeField(format='iso-8601',required=False)
    dateBetweenStart = serializers.DateField(format='iso-8601', required=False)
    dateBetweenEnd = serializers.DateField(format='iso-8601', required=False)
    latitudeBetweenStart = serializers.DecimalField(max_digits=9,decimal_places=6,max_value=90, min_value=-90,required=False)
    latitudeBetweenEnd = serializers.DecimalField(max_digits=9,decimal_places=6,max_value=90, min_value=-90,required=False)
    longitudeBetweenStart = serializers.DecimalField(max_digits=9,decimal_places=6,max_value=180, min_value=-180,required=False)
    longitudeBetweenEnd = serializers.DecimalField(max_digits=9,decimal_places=6,max_value=180, min_value=-180,required=False)
    city = serializers.CharField(required=False)
    district = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    sport = serializers.CharField(required=False)
    skillLevel = serializers.ListField(
        child=serializers.IntegerField(
            min_value=0, max_value=10), required=False
    )

    def validate(self, data):
        if ((('latitudeBetweenStart' in data) and ('latitudeBetweenEnd' not in data)) or ('latitudeBetweenStart' not in data) and (('latitudeBetweenEnd' in data))):
            raise serializers.ValidationError({"latitude": "latitudeBetweenStart and latitudeBetweenEnd must be given together."})

        if ((('longitudeBetweenStart' in data) and ('longitudeBetweenEnd' not in data)) or ('longitudeBetweenStart' not in data) and (('longitudeBetweenEnd' in data))):
            raise serializers.ValidationError({"longitude": "longitudeBetweenStart and longitudeBetweenEnd must be given together."})
        
        if ('timeBetweenStart'in data) and ('timeBetweenEnd' in data) and (data['timeBetweenStart'] > data['timeBetweenEnd']):
            raise serializers.ValidationError({"time": "timeBetweenStart should be smaller than or equal to timeBetweenEnd"})   
        
        if ('dateBetweenStart'in data) and ('dateBetweenEnd' in data) and (data['dateBetweenStart'] > data['dateBetweenEnd']):
            raise serializers.ValidationError({"date": "dateBetweenStart should be smaller than or equal to dateBetweenEnd"})   

        if ('latitudeBetweenStart' in data) or ('longitudeBetweenStart' in data): # city etc should not be given
            if 'city' in data:
                raise serializers.ValidationError({"city": "city and coordinate information must not be given together"})   
            if 'district' in data:
                raise serializers.ValidationError({"district": "district and coordinate information must not be given together"})   
            if 'country' in data:
                raise serializers.ValidationError({"country": "country and coordinate information must not be given together"})   

        return data