# coding: utf-8

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, EntryViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('entries', EntryViewSet)

urlpatterns = [
    path('users/', UserViewSet, name='users'),
]
