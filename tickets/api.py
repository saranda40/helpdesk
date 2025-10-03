from .models import Ticket
from rest_framework import viewsets, permissions
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = TicketSerializer