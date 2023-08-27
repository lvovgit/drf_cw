from rest_framework import serializers

from habbits.models import Habit
from habbits.validators import excludeValidator

class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [excludeValidator]