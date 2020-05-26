from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rooms.models import Room
from .serializers import ReadUserSerializer
from rooms.serializers import RoomSerializer

# Create your views here.


class MeView(APIView):
    """ MeView Class Definition """

    def get(self, request):
        # 사용자 profile 확인할 수 있는 권한 있는지 체크
        if request.user.is_authenticated:
            return Response(ReadUserSerializer(request.user).data)

    def put(self, request):
        pass


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class FavsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = RoomSerializer(user.favs.all(), many=True).data
        return Response(serializer)

    # Favs update
    def put(self, request):
        # room pk 체크
        pk = request.data.get("pk", None)
        user = request.user
        if pk is not None:
            try:
                # room이 존재하는 지 확인
                room = Room.objects.get(pk=pk)
                # room의 정보가 user의 fav에 있다면 삭제, 없으면 추가
                if room in user.favs.all():
                    user.favs.remove(room)
                else:
                    user.favs.add(room)
                return Response()
            except Room.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)
