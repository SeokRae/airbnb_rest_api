from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer


# Create your views here.

# ListRoom
class ListRoomsView(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# See Room
class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
