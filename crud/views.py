from rest_framework import generics
from .models import UserTable
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = UserTable.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = UserTable.objects.all()
    serializer_class = UserSerializer