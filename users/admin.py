from django.contrib import admin
from .models import User


@admin.register(User)
class HabbitAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'is_active',)
    list_filter = ('id',)