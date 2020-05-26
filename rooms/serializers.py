from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


# Data Serializers
class RoomSerializer(serializers.ModelSerializer):
    """ Room Serializers """

    # room create, update 시 user 객체는 validate하지 않도록 설정
    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)
        # user의 정보인 내용은 read_only로 설정
        read_only_fields = ("user", "id", "created", "updated")

    def validate(self, data):
        # instance가 존재하는 경우(Create) check_in, check_out 데이터의 validate check
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")
        return data
