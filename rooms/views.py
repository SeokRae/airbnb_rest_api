from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


# Create your views here.


class RoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()[:5]
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)

    def post(self, request):

        # POST할 수 없는 사용자 권한 체크 > 401
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)

        # serializer의 데이터가 유효할경우 Create
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    # default get_room
    def get_room(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    # 요청 값에 따른 get
    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = ReadRoomSerializer(room).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # room 작성하기
    def put(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            # instance: room 값을 첫번째 파라미터로 넣으면 이를 update로 인식하여 동작
            # partial = True 값의 뜻은 모든 데이터를 보내지 않고, 내가 바꾸고 싶은 데이터만 전송할 수 있게 하겠다는 뜻
            serializer = WriteRoomSerializer(room, data=request.data, partial=True)
            # room 작성 입력값 체크
            if serializer.is_valid():
                room = serializer.save()
                # update된 room 데이터를 조회
                return Response(ReadRoomSerializer(room).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # room 삭제
    def delete(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            # 권한 체크
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
