from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer


# ----------- MENU ITEM VIEWS -----------
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    # Uncomment this if you want menu to be protected
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    # Uncomment to require token
    permission_classes = [IsAuthenticated]


# ----------- BOOKING VIEWSET -----------
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    permission_classes = [IsAuthenticated]


# ----------- PROTECTED MESSAGE VIEW -----------
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})
