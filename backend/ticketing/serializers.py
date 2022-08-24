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
        stored = Ticket.objects.latest('number')
        print("lates number: ")
        print(stored)
        ticket.number = Ticket.objects.latest('number').number + 1
        print("new number: ")
        print(ticket.number)
        ticket.save()
        return ticket
