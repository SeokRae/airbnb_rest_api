from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
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

    def put(self, request):
        pass
