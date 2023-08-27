from habbits.models import Habit
from habbits.serializers.serializers import HabitSerializers
from habbits.pagination import HabitPagination
from users.models import UserRoles
from rest_framework import viewsets, generics
from rest_framework import viewsets, generics

from habbits.models import Habit
from habbits.pagination import HabitPagination
from habbits.serializers.serializers import HabitSerializers
from users.models import UserRoles


# Create your views here.

class HabbitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def perform_create(self, serializer) -> None:
        """Сохраняет новому объекту владельца"""
        serializer.save(owner=self.request.user)

    # def perform_update(self, serializer):
    #     self.object = serializer.save()
    #     send_mail_user_update.delay(self.object.pk)

    def get_queryset(self):  # перечень привычек доступный пользователю или модератору
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabbitsListView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        """Список публичных привычек"""
        user = self.request.user

        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(public=True)
