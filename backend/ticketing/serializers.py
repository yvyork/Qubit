from django.utils import timezone
from .models import Ticket
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Ticket
        fields = ['id', 'number', 
            'timestamp', 'wait', 'called', 'counter']
       
    def create(self, validated_data):  
        ticket = Ticket(**validated_data)
        ticket.ticket_timestamp = timezone.now()
        ticket.number = Ticket.objects.latest('number').number + 1
        ticket.save()
        return ticket
