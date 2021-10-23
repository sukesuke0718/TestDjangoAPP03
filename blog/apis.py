from rest_framework import viewsets, routers
from .models import User, Entry
from .serializer import UserSerializer,EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('entries', EntryViewSet)
