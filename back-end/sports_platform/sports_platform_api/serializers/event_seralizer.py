from rest_framework import serializers
from ..models.event_models import Event

class EventSerializer(serializers.ModelSerializer):
     class Meta:
        model = Event
        exclude = ['latitude', 'longitude', 'city', 'district', 'country',
                  'minimumAttendeeCapacity', 'maxSpectatorCapacity','acceptWithoutApproval']