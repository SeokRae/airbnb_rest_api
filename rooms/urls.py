from django.urls import path

# from . import views
from rest_framework.routers import DefaultRouter
from . import viewsets

app_name = "rooms"

# urlpatterns = [
#     path("list/", views.ListRoomsView.as_view()),
#     path("<int:pk>/", views.DetailRoomView.as_view()),
# ]

router = DefaultRouter()
router.register("", viewsets.RoomViewset, basename="room")

urlpatterns = router.urls
