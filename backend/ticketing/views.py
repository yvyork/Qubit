from os import stat
import re
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services.printing import PDF
from .services.paul import callPaul
from .models import Ticket
from .serializers import TicketSerializer



@api_view(['GET', 'POST', 'PUT'])
def ticket_list(request):
    if request.method == 'GET':       
        queryset = Ticket.objects.select_related('counter').all()
        called = request.query_params.get('called')
        if called:
            queryset = queryset.filter(called=called)
        serialzer = TicketSerializer(queryset, many=True)
        return Response(serialzer.data)
    elif request.method == 'POST':
        serialzer = TicketSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        # PDF.printTicket(serialzer.data['number'])
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
       
@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail(request, id):
    if request.method == 'GET':
        ticket = get_object_or_404(Ticket, pk=id)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    elif request.method == 'PUT':
        ticket = get_object_or_404(Ticket, pk=id)
        serialzer = TicketSerializer(ticket, data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        # callPaul(ticket.number, ticket.counter)
        return Response(serialzer.data)
    elif request.method == 'DELETE':
        ticket = get_object_or_404(Ticket, pk=id)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

