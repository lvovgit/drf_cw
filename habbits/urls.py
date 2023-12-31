from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()
router.register(r'habits', HabbitsViewSet, basename='habits')


urlpatterns = [
                  path('public_habits/', HabbitsListView.as_view(), name='habits_list'),

              ] + router.urls